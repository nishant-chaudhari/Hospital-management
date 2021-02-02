from odoo import api, fields, models

class appointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'appointment details'

    name = fields.Char(string = 'Name',required='true',)
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
    other_details = fields.Text(string = 'Other Details' )



    #    #********************************** SELF ************************************
    # def btn_selfenv(self):
    #     print("=================== self ==================", self)
    #     print("=================== self.env==================", self.env)
    #     print("=================== self.env.context ==================", self.env.context)
    #     print("=================== self.env.context.get('uid') ==================", self.env.context.get('uid'))

    #    #****************************** Search in RS(Record Set) ********************************

    def btn_selfenv(self):
        # print("======================= creating blank RS ====================")
        # record = self.env['hospital.appointment']
        # print("======================= blank RS print ====================",record)
 
        # record = self.env['hospital.appointment'].search([])
        # print("======================= RS print with search method ====================",record)

        record = self.env['hospital.appointment'].search([('contact','=','8200712493')])
        for rec in record:
            print(rec.name)
        print("======================= RS print with search method ====================",record)

    #    #****************************** Browse ********************************
    # def btn_selfenv(self):
    #     record = self.env['hospital.appointment'].browse([1,3])
    #     print("======================= Called Mapped ====================",record)

    #    #****************************** Mapped ********************************

    # def btn_mapped(self):
    #     record = self.env['hospital.appointment'].search([]).mapped('email')
    #     print("======================= Called Mapped ====================",record)

    #    #****************************** Filtered ********************************

    # def btn_filtered(self):
    #     record = self.env['hospital.appointment'].search([]).filtered(lambda a: a.name == 'Abid Bhagat')
    #     print("======================= Filtered Called ====================",record)

    #    #****************************** Sorted ********************************

    # def btn_sorted(self):
    #     record = self.env['hospital.appointment'].search([]).sorted('name')
    #     # record = sorted(self.env['hospital.appointment'].search([]).filtered(lambda a: a.age > 25).mapped('name'))
    #     print("======================= Sorted Called ====================", record)


# # ************************************ ORM Method ******************************************

    #    #****************************** default_get ********************************

    # @api.model
    # def default_get(self, fields_list):
    #     # print('******************* Default Get Called **********************')
    #     # print('******************* Default get field list *******************',fields_list)
    #     res = super(appointment,self).default_get(fields_list)
    #     print('********************** After Super Call res *************************')
    #     print('*********************** Res *************************',res)
    #     return res

    #    #****************************** search ********************************

    # @api.model
    # def search(self, args, offset=0, limit=None, order=None, count=False):
    #     # args = [('name','ilike','asad')]
    #     # print('******************* field list *******************',args)
    #     res = super(appointment,self).search(args=args,offset=offset,limit=limit,order=order,count=False)
    #     print('********************** After Super Call res *************************')
    #     print('*********************** Res *************************',res)
    #     return res

#    #****************************** search_read ********************************

    # @api.model
    # def search_read(self,domain=None,fields=None,offset=0,limit=None,order=None):
    #     print('******************* search read method called *******************')
    #     print('******************* field list *******************',fields)
    #     res = super(appointment,self).search_read(domain=[('name','=','Abid')],fields=['name'],offset=offset,limit=limit,order=order)
    #     # res = super(appointment,self).search_read(domain=None, fields=fields, offset=offset, limit=limit,order=order)
    #     print('*********************** Res super called *************************',res)
    #     return res

#    #****************************** Create Method ********************************

    # @api.model
    # def create(self,vals_list):
    #     print('******************* Create method called *******************')
    #     print('******************* cre_list *******************',vals_list)
    #     vals_list['age']=35
    #
    #     res = super(appointment,self).create(vals_list=vals_list)
    #     print('******************* res super called *******************',res)
    #     return res

#    #****************************** Unlink Method ********************************

    # def unlink(self):
    #     print('******************* Unlink method called *******************')
    #     x = super(appointment, self).unlink()
    #     print('******************* method called X *******************',x)
    #     return x

#    #****************************** Write Method ********************************

    # def write(self,abc):
    #     print('******************* Write method called *******************')
    #     print('******************* vals *******************',abc)
    #     # for rec in self:
    #     #     if rec.name == 'Abid':
    #     #         abc['age'] = 50
    #     # print('******************* ABC *******************',abc)
    #     abc.update({'age':'18'})
    #     print('******************* ABC *******************', abc)
    #     res = super(appointment, self).write(vals=abc)
    #     print('******************* res *******************', res)
    #     return res

#    #****************************** Copy Method ********************************

    # def copy(self, default=None):
    #     print('******************* Copy method called *******************')
    #     default = {}
    #     default['name']='Neets'
    #     res = super(appointment, self).copy(default=default)
    #     print('******************* res *******************',res)
    #     return res

#    #****************************** Search_Count Method ********************************
#     def btn_selfenv(self):
        # print('******************* Create Blank record set *******************')
        # record = self.env['hospital.appointment']
        # print('******************* record *******************',record)

        # record = self.env['hospital.appointment'].search_count([])
        # print('******************* rs print with search_count method *******************', record)

        # record = self.env['hospital.appointment'].search_count([('name','=','Asad')])
        # print('******************* rs print with search_count method *******************', record)

#    #****************************** Read_group Method ********************************

    # @api.model
    # def read_group(self, domain, fields, groupby, offset=0, limit=None, orderby=False, lazy=True):
    #     print('**************************** Read_group called ***************************')
    #     print('**************************** fields ***************************',fields)
    #     # res = super(appointment, self).read_group(domain=[('name','=','Asad')],fields=['contact_no'],groupby=groupby,offset=offset,limit=limit,orderby=orderby,lazy=lazy)
    #     res = super(appointment, self).read_group(domain=domain,fields=fields,groupby=groupby,offset=offset,limit=limit,orderby=orderby,lazy=lazy)
    #     print('************************* res ***************************',res)
    #     # for i in res:
    #     #     print(i)
    #     return res

#    #****************************** ORM fields_view_get Method ********************************

    # @api.model
    # def fields_view_get(self, view_id='view_hospital_doctor_tree',view_type='tree',toolbar=False,submenu=False):
    #     print('**************** fields_view_get called ********************')
    #     res = super(appointment,self).fields_view_get(view_id=view_id, view_type=view_type,toolbar=False, submenu=False)
    #     # res['fields']['name']['sortable']=False
    #     res['fields']['name']['string']='Patient Name'
    #     print('**************** res *****************',res)
    #     return res