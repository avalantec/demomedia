from odoo import api, fields, models
import logging

log = logging.getLogger(__name__)

#1612508304
class CrmLeadProgramType(models.Model):
    _name = "crm.lead.program_type"
    _description = 'CRM Lead Program Type'
    
    name = fields.Char("Program Type")