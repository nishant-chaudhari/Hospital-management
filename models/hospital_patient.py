from odoo import api, fields, models

class patient(models.Model):
    _name = 'hospital.patient'
    _description = 'patient details'
    _sql_constraints = [
        ('unique_mobile','UNIQUE(contact_no)','Mobile number is already registred ! :',)
    ]

    name = fields.Char(string = 'Name',required='true')
    age = fields.Integer(string = 'Age')
    gender = fields.Selection([('male','Male'),
                               ('female','Female')
                               ],string = 'Gender',default='male')
    contact_no = fields.Char(string = 'Mobile No',size=14 )
    email = fields.Char(string = 'Email')
    address = fields.Text(string = 'Address')
    image = fields.Binary(string='Image')
    state = fields.Many2one('res.country.state',string='State')
    country = fields.Many2one('res.country',string='Country')

    doctor_id = fields.Many2one(comodel_name = 'hospital.doctor', string = 'Under Treatment of Dr.')
    room_id = fields.Many2one(comodel_name='hospital.room', string='Room No')
    admit_date = fields.Date(string='Admit Date')

