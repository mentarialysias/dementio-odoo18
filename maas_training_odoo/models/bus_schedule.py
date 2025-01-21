from odoo import models, fields, api
from datetime import date
from odoo.exceptions import ValidationError

class BusSchedule(models.Model):
    _name = 'bus.schedule'
    _description = 'Bus Schedule'

    name = fields.Char(string='Name')
    # schedule = fields.Datetime(string='Schedule')
    
    payment_method = fields.Selection([
        ("cash","Cash"),
        ("transfer","Transfer")
    ], string='Payment Method')
    departure = fields.Datetime(string="Departure")
    arrival = fields.Datetime(string="Arrival")
    bus_id = fields.Many2one('res.bus', string='Bus')
    route_id = fields.Many2one('bus.route', string='Route')
    baggage_ids = fields.One2many('baggage.baggage', 'schedule_id', string='Baggage')
    passenger_ids = fields.Many2many('res.passenger', string='Passenger')
    capacity = fields.Integer(
        string='Capacity',
        related='bus_id.capacity',
    )
    
    date_of_issue = fields.Date(
        string='Date of Issue', 
        default=lambda self: date.today()
    )

    driver_id = fields.Many2one(
        'hr.employee',
        string='Driver',
        domain=[('is_driver', '=', True)],  # Filter hanya untuk driver
    )
    
    @api.constrains('departure', 'arrival')
    def _check_departure_and_arrival(self):
        for record in self:
            if record.arrival and record.departure and record.arrival < record.departure:
                 raise ValidationError("Arrival time cannot be earlier than Departure time.")
            
    @api.constrains('passenger_ids', 'capacity')
    def _check_passenger_capacity(self):
        for record in self:
            if record.passenger_ids and len(record.passenger_ids) > record.capacity:
                raise ValidationError(
                    f"The number of passengers ({len(record.passenger_ids)}) exceeds the bus capacity ({record.capacity})."
                )
   