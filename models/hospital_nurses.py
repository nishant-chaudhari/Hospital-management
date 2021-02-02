from odoo import api, fields, models

class nurses(models.Model):
    _name = 'hospital.nurses'
    _description = 'nurses details'

    name = fields.Char(string = 'Name')
    age = fields.Integer(string = 'Age')
    gender = fields.Selection([('male','Male'),
                               ('female','Female'),
                               ],string = 'Gender')
    contact_no = fields.Char(string = 'Mobile No')
    address = fields.Text(string = 'Address')
    image = fields.Binary(string = 'Image')