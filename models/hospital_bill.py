from odoo import api, fields, models

class bill(models.Model):
    _name = 'hospital.bill'
    _description = 'Billing details'
    _rec_name = 'bill_no'

    bill_no = fields.Char(string = 'Bill No')
    bill_id = fields.Many2one(comodel_name='hospital.patient', string='Name')
    mob_no = fields.Char(related='bill_id.contact_no',string='Mob No')
    address = fields.Text(related='bill_id.address',string='Address')

    dr_charge = fields.Float(string = 'Dr. Charges')
    room_charge = fields.Float(string = 'Room Charge')

    medicines = fields.Float(string = 'Total Amount Of Medicines')
    medicines_disc = fields.Integer(string = 'Discount on Medicines',default =10,readonly='1')
    medicines_total = fields.Float(string='Payable Amount Of Medicines',compute='calc_disc_medicine')

    total_bill = fields.Float(string='Total Bill',compute='calc_total_bill')

    # For state
    state = fields.Selection([
        ('cancel','cancel'),
        ('confirmed','Confirmed')
    ], string='state',default="cancel")

    def btn_confirm(self):
        self.state = "confirmed"

    def btn_cancel(self):
        self.state = "cancel"



    # For Compute
    def calc_disc_medicine(self):
        for rec in self:
            rec.medicines_total=rec.medicines-(rec.medicines*rec.medicines_disc)/100

    # Compute total
    def calc_total_bill(self):
        for i in self:
            i.total_bill=i.dr_charge+i.medicines_total+i.room_charge
