from odoo import models, fields, api 

class ResStudent(models.Model):
    _name = 'res.student'
    _description = 'Student'

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    nim = fields.Char(string='NIM')
    class_id = fields.Many2one('class.class', string='Kelas')

