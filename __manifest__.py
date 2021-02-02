{

    'name': 'hospital',
    'summary': 'A Module that manages all the process of Hospital ',
    'version': '1.0',
    'author': 'Techultra Solutions',
    'website': 'www.techultrasolutions.com',

    'depends': ['base'],
    'data': [

        'security/hospital_security.xml',
        'security/ir.model.access.csv',

        'views/hospital_patient_view.xml',
        'views/hospital_doctor_view.xml',

        'views/hospital_room_view.xml',
        'views/hospital_bill_view.xml',
        'views/hospital_nurses_view.xml',
        'views/hospital_otherstaff_view.xml',
        'views/hospital_appointment_view.xml',

    ],

    'installable': True,
    'application': True,
    'auto_install': False,

}
