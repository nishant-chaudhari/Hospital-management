from odoo import api, fields, models

class doctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'doctor details'

    name = fields.Char(string = 'Name')
    age = fields.Integer(string = 'Age')
    gender = fields.Selection([('male','Male'),
                               ('female','Female'),
                               ],string = 'Gender')
    contact_no = fields.Char(string = 'Mobile No')
    designation = fields.Char(string='Designation')
    address = fields.Text(string = 'Address')
    image = fields.Binary(string = 'Image')


    patient_ids = fields.One2many(comodel_name='hospital.patient', inverse_name='doctor_id', string = 'Patient')

    count_patient = fields.Integer(string='patient', compute='get_patient_count')

    def btn_patient(self):
        return {
            'name': 'branch of staff',
            'type': 'ir.actions.act_window',
            'res_model': 'hospital.patient',
            'view_mode': 'tree,form',
            'domain':[('doctor_id','=',self.id)],
        }

    def get_patient_count(self):
        count = self.env['hospital.patient'].search_count([('doctor_id', '=', self.id)])
        self.count_patient = count

#    #****************************** ORm name_get Method ********************************

    # def name_get(self):
    #     print("************* Name_Get Called ***********")
    #     nget_list = []
    #     for i in self:
    #         na = i.name + ':' + str(i.age)
    #         nget_list.append((i.id,na))
    #     return nget_list

#    #********************************* ORM name_search Method **********************************

    # @api.model
    # def name_search(self,name='',args=None,operator='ilike',limit=100):
    #     domain = ['|',('name',operator,name),('designation',operator,name)]
    #     args += domain
    #     i_rs = self.search(args,limit=limit)
    #     return i_rs.name_get()
    #     print('********************** Name_Search*************************')

#    #*********************************  **********************************