from odoo import models, fields, api

class ResBus(models.Model):
    _name = 'res.bus'
    _description = 'Bus'

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code', required=True)
    capacity = fields.Integer(string="Capacity", required=True)
    image = fields.Binary(string='Image')

    _sql_constraints = [
            ('unique_code', 'unique(code)', 'The Bus Code must be unique.')
        ]
    