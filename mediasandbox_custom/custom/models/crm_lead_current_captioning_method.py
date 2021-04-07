from odoo import api, fields, models
import logging

log = logging.getLogger(__name__)

#1612508304
class CrmLeadCurrentCaptioningMethod(models.Model):
    _name = "crm.lead.current_captioning_method"
    _description = 'CRM Lead Current Captioning Method'
    
    name = fields.Char("Current Captioning Method")