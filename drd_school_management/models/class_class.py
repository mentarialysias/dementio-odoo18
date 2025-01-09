from odoo import models, fields, api 

class Class(models.Model):
    _name = 'class.class'
    _description = 'Class'

    name = fields.Char(string='Name', required=True)
    total_student = fields.Integer(string='Total Student', compute='_compute_total_student')
    is_active = fields.Boolean(string='Is Active')
    student_ids = fields.One2many(
        comodel_name='res.student',
        inverse_name='class_id',
        string='Students',
    )
    
    def _compute_total_student(self):
        for rec in self:
            rec.total_student = len(rec.student_ids)

    
