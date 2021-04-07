from odoo import api, fields, models
import logging

log = logging.getLogger(__name__)

#1612508304
class CrmLeadPrimaryService(models.Model):
    _name = "crm.lead.primary_service"
    _description = 'CRM Lead Primary Service Type'
    
    name = fields.Char("Primary Service")