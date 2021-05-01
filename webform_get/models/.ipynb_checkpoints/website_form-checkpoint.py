# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

from odoo.exceptions import ValidationError

from odoo.addons.website_form.controllers.main import WebsiteForm

import logging
_logger = logging.getLogger(__name__)


class CustomWebsiteForm( WebsiteForm ):
    #1616781080
    def _handle_website_form(self, model_name, **kwargs):
        
        model_record = request.env['ir.model'].sudo().search([
            ('model', '=', model_name), ('website_form_access', '=', True)
        ])
        
        if not model_record:
            return json.dumps({
                'error': _("The form's specified model does not exist")
            })

        try:
            #1616781087
            data_success_page = ""
            
            for param in list(request.params):
                if param == "data_success_page":
                    data_success_page = request.params[param]
                    del request.params[param]
                    continue
                
                if str( type( request.params[param] ) ) == "<class 'werkzeug.datastructures.FileStorage'>":
                    #1618605477
                    data1 = request.params[param].getvalue()
                    data1_len = len( data1 )
                    if data1_len == 0:
                        del request.params[param]
                        continue
            
            data = self.extract_data(model_record, request.params)
            
        # If we encounter an issue while extracting data
        except ValidationError as e:
            # I couldn't find a cleaner way to pass data to an exception
            return json.dumps({'error_fields' : e.args[0]})

        try:
            id_record = self.insert_record(request, model_record, data['record'], data['custom'], data.get('meta'))
            if id_record:
                self.insert_attachment(model_record, id_record, data['attachments'])
                # in case of an email, we want to send it immediately instead of waiting
                # for the email queue to process
                if model_name == 'mail.mail':
                    request.env[model_name].sudo().browse(id_record).send()

        # Some fields have additional SQL constraints that we can't check generically
        # Ex: crm.lead.probability which is a float between 0 and 1
        # TODO: How to get the name of the erroneous field ?
        except IntegrityError:
            return json.dumps(False)

        request.session['form_builder_model_model'] = model_record.model
        request.session['form_builder_model'] = model_record.name
        request.session['form_builder_id'] = id_record

        #1616781095
        if id_record:
            if data_success_page:
                #data_success_page = "https://{}".format( data_success_page )
                return http.request.redirect( data_success_page   )
            else:
                return json.dumps({'id': id_record})
        else:
            return "ERROR: Record Not Created"
