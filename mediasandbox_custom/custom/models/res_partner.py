from odoo import api, fields, models
import logging

log = logging.getLogger(__name__)

class Partner(models.Model):
    _inherit = "res.partner"
    _description = 'Res Partner Inherit'
    
    first_name = fields.Char("First Name")
    last_name = fields.Char("Last Name")
    
    fax = fields.Char("Fax")
    phone_ext = fields.Char()
    
    phone2 = fields.Char("Phone 2")
    
    phone2_ext = fields.Char()
    person_type = fields.Many2one("res.partner.person_type", string="Person Type")
    primary_service = fields.Many2one("crm.lead.primary_service", string="Primary Service")

    @api.onchange('first_name', 'last_name')
    def _onchange_first_name_last_name(self):
        if self.first_name or self.last_name:
            if not self.first_name:
                self.first_name = ""
            if not self.last_name:
                self.last_name = ""
            self.name = self.first_name + " " + self.last_name

    @api.onchange('phone2', 'country_id', 'company_id')
    def _onchange_phone2_validation_test(self):
        if self.phone2 and self.country_id:
            self.phone2 = self.phone_format(self.phone2)

    @api.onchange('fax', 'country_id', 'company_id')
    def _onchange_fax_validation_test(self):
        if self.fax and self.country_id:
            self.fax = self.phone_format(self.fax)
             
    @api.model
    def default_get(self, fields):
        rec = super(Partner, self).default_get(fields)
        active_model = self.env.context.get('active_model')
        if active_model == 'crm.lead' and len(self.env.context.get('active_ids', [])) <= 1:
            lead = self.env[active_model].browse(self.env.context.get('active_id')).exists()
            if lead:
                rec.update(
                    phone=lead.phone,
                    mobile=lead.mobile,
                    function=lead.function,
                    title=lead.title.id,
                    website=lead.website,
                    street=lead.street,
                    street2=lead.street2,
                    city=lead.city,
                    state_id=lead.state_id.id,
                    country_id=lead.country_id.id,
                    zip=lead.zip,
                    first_name=lead.first_name,
                    last_name=lead.last_name,
                    fax=lead.fax,
                    phone_ext=lead.phone_ext,
                    phone2=lead.phone2,
                    phone2_ext=lead.phone2_ext,
                    industry_id=lead.industry_id.id,
                    primary_service=lead.primary_service.id,
                )
        return rec

