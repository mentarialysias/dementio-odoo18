from odoo import models, fields, api

class ResSubject(models.Model):
    _name = 'res.subject'
    _description = 'Subject'

    name = fields.Char(string='Name')
    sks = fields.Integer(string='SKS')
    lecture  = fields.Char(string='Lecture')
    duration = fields.Float(string='Duration')
    schedule_ids = fields.One2many(
        comodel_name='schedule.line',
        inverse_name='subject_id',
        string='Schedules',
    )

    
    