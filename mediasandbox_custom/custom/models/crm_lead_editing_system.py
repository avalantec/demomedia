from odoo import api, fields, models
import logging

log = logging.getLogger(__name__)

#1612508304
class CrmLeadEditingSystem(models.Model):
    _name = "crm.lead.editing_system"
    _description = 'CRM Lead Editing System'
    
    name = fields.Char("Editing System")