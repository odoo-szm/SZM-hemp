# -*- coding: utf-8 -*-
{
    'name': "psi_web_module",

    'summary': """
        SZM hemp supply website""",

    'description': """
        A custom website for SZM
    """,

    'author': "Precisonline",
    'website': "http://www.precisionline.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'website'    
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    
    'installable': True,
    'application': False,
    'auto_install': False,
}

