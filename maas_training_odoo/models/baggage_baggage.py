from odoo import models, fields, api

class BaggageBaggage(models.Model):

    _name = 'baggage.baggage'
    _description = 'Baggage'

    name = fields.Char(string='Name')
    weight = fields.Float(string='Weight(Kg)')
    schedule_id = fields.Many2one('bus.schedule', string='Shedule ID',)