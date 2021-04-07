from odoo import api, fields, models
import logging

log = logging.getLogger(__name__)

#1612508304
class CrmLeadNativeFormat(models.Model):
    _name = "crm.lead.native_format"
    _description = 'CRM Lead Native Format'
    
    name = fields.Char("Native Format")