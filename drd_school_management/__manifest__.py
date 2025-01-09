# -*- coding: utf-8 -*-
{
    'name': "School Management",

    'summary': "Modul ini digunakan untuk management school",

    'description': """
Long description of module's purpose
    """,

    'author': "Dementio",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '18.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/class_view.xml',
        'views/student_view.xml',
        'views/subject_view.xml',
        'views/schedule_view.xml',
        'views/hr_employee_view.xml',
        'views/menuitems.xml'
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

