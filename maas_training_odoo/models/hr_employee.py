from odoo import models, fields, api 

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    is_driver = fields.Boolean(string='Is Driver')
    driver_license = fields.Char(string='Driver License')
    driver_license_expired_date = fields.Date(string='Driver License Expiry Date')