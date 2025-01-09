from odoo import models, fields, api
from datetime import timedelta

class ScheduleLine(models.Model):
    _name = 'schedule.line'
    _description = 'Schedule Line'

    start_time = fields.Datetime(string="Start Time")
    end_time = fields.Datetime(string="End Time", compute="_compute_end_time", store=True)
    duration = fields.Float(string="Duration (Hours)", related="subject_id.duration", readonly=True)
    subject_id = fields.Many2one(comodel_name='res.subject', string='Subjects')

    @api.depends('start_time', 'duration')
    def _compute_end_time(self):
        for record in self:
            if record.start_time and record.duration:
                # Menambahkan durasi (dalam jam) ke start_time
                record.end_time = record.start_time + timedelta(hours=record.duration)
            else:
                record.end_time = False
