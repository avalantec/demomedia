from odoo import api, fields, models
import logging

log = logging.getLogger(__name__)

#1612508304
class CrmLeadEmail(models.Model):
    _name = "crm.lead.email_status"
    _description = 'CRM Lead Email Status'
    
    name = fields.Char("Email Status")