from odoo import models, fields, api

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    role = fields.Selection([
        ("teacher","Teacher"),
        ("student","Student"),
        ("staff", "Staff")
    ], string='Roles', default="student")




