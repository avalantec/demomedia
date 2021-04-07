from odoo import api, fields, models
import logging

log = logging.getLogger(__name__)

#1612508304
class CrmLeadProgramFrequency(models.Model):
    _name = "crm.lead.program_frequency"
    _description = 'CRM Lead Program Frequency'
    
    name = fields.Char("Program Frequency")