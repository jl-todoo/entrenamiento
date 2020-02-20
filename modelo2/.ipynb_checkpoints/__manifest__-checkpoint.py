# -*- coding: utf-8 -*-
{
    'name': "modelo2",

    'summary': """
        creacion de ventas odoo""",

    'description': """
        En este encontraras todo lo relacionado con sales del sistema odoo
    """,

    'author': "Jonathan Leon",
    'website': "http://www.proposito.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'sales',
    'version': '1.5',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
   #     'views/templates.xml',
    ],
    # only loaded in demonstration mode
#    'demo': [
 #       'demo/demo.xml',
  #  ],
        "installable": True,
}
