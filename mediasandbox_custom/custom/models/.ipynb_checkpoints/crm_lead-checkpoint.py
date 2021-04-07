from odoo import api, fields, models
import logging

log = logging.getLogger(__name__)

class CrmLead(models.Model):
    _inherit = "crm.lead"
    _description = 'CRM Lead Inherit'

    
    #1612499847
    first_name = fields.Char("First Name")
    last_name = fields.Char("Last Name")
    
    @api.onchange('first_name', 'last_name')
    def _onchange_first_name_last_name(self):
        if self.first_name or self.last_name:
            if not self.first_name:
                self.first_name = ""
            if not self.last_name:
                self.last_name = ""
            self.contact_name = self.first_name + " " + self.last_name
    
    
    #1612500380
    fax = fields.Char("Fax")
    
    @api.onchange('fax', 'country_id', 'company_id')
    def _onchange_fax_validation_test(self):
        if self.fax and self.country_id:
            self.fax = self.phone_format(self.fax)
 
    #1612501149
    phone_ext = fields.Char()
    
    #1612500349
    phone2 = fields.Char("Phone 2")
    phone2_ext = fields.Char()
    
    @api.onchange('phone2', 'country_id', 'company_id')
    def _onchange_phone2_validation_test(self):
        if self.phone2 and self.country_id:
            self.phone2 = self.phone_format(self.phone2)
    
    #1612507126
    person_type = fields.Many2one("res.partner.person_type", string="Person Type")
    
    #1612508304
    email_status = fields.Many2one("crm.lead.email_status", string="Email Status")
    
    #1612509915
    primary_service = fields.Many2one("crm.lead.primary_service", string="Primary Service")

    #1612510580
    industry_id = fields.Many2one("res.partner.industry", string="Organization Type")
    
    #1612636904
    editing_system_id = fields.Many2one("crm.lead.editing_system", string="Editing System")
    
    #1612636904
    native_format_id = fields.Many2one("crm.lead.native_format", string="Native Format")
    
    #1612637496
    show_name = fields.Char("Show Name")
    
    #1612637754
    program_frequency_id = fields.Many2one("crm.lead.program_frequency", string="Program Frequency")
    
    #1612638294
    program_type_id = fields.Many2one("crm.lead.program_type", string="Program Type")
    
    #1612638632
    current_captioning_method_id = fields.Many2one("crm.lead.current_captioning_method", string="Current Captioning Method")
    
    #1612640458
    fcc_exemption_file = fields.Char("FCC Exemption File #")
