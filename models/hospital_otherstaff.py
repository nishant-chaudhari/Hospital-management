from odoo import api, fields, models

class otherstaff(models.Model):
    _name = 'hospital.otherstaff'
    _description = 'otherstaff details'

    name = fields.Char(string = 'Name')
    age = fields.Integer(string = 'Age')
    gender = fields.Selection([('male','Male'),
                               ('female','Female'),
                               ],string = 'Gender')
    contact_no = fields.Char(string = 'Mobile No')
    address = fields.Text(string = 'Address')
    select_position = fields.Selection([('clinical assistants','Clinical Assistants'),
                                        ('volunteers','Volunteers'),
                                        ('ward clerks','Ward Clerks'),
                                        ('ward boy','Ward Boy')])
    image = fields.Binary(string = 'Image')