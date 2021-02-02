from odoo import api, fields, models

class room(models.Model):
    _name = 'hospital.room'
    _description = 'Room details'
    _rec_name = 'room_no'

    room_no = fields.Integer(string = 'Room No')
    room_type = fields.Selection([('general ward','General Ward'),
                                ('private room','Private Room'),
                                ('deluxe room','Deluxe Room'),
                                ('suite','Suite'),
                                   ],string = 'Room Type')
    room_charge = fields.Char(string='Room Charge')
    available = fields.Boolean(string='available')