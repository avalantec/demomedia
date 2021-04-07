from odoo import api, fields, models
import logging

log = logging.getLogger(__name__)

#1612508771
class PersonType(models.Model):
    _name = "res.partner.person_type"
    _description = 'Res Partner Person Type'
    
    name = fields.Char("Person Type")