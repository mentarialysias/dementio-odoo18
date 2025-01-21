from odoo import models, fields, api
from datetime import date

class ResPassenger(models.Model):
    _name = 'res.passenger'
    _description = 'Passenger'

    name = fields.Char(string='Name')
    weight = fields.Float(string='Weight(Kg)')
    height = fields.Float(string='Height(Cm)')
    birth_date = fields.Date(string='Birth Date')

    age = fields.Integer(
        string='Age',
        compute='_compute_age'
    )

    @api.depends('birth_date')
    def _compute_age(self):
        for record in self:
            if record.birth_date:
                today = date.today()
                delta = today.year - record.birth_date.year
                if today.month < record.birth_date.month or (today.month == record.birth_date.month and today.day < record.birth_date.day):
                    delta -= 1
                record.age = delta
            else:
                record.age = 0