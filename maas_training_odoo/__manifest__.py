# -*- coding: utf-8 -*-
{
    'name': "maas_training_odoo",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/bus_route_view.xml',
        'views/bus_schedule_view.xml',
        'views/hr_employee_view.xml',
        'views/res_bus_view.xml',
        'views/res_passenger_view.xml',
        'views/baggage_baggage_view.xml',
        # 'views/_view.xml',
        'views/menuitems.xml'
        
    ],
}

