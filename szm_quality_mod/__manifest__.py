# -*- coding: utf-8 -*-
{
    'name': 'SZM Quality Module Enhancement',

    'summary': 'Enhancement to Quality Alert and Control Points',

    'description': """
        09-17-20 -  Jeff Mueller, Add attributes to QA Module to facilitate
                    tracking of Quality control reporting for GFSI requirements.
    """,

    'author': "Precision Solutions, Inc",
    'website': "http://www.precisonline.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Quality',
    'sequence': 50,
    'version': '0.1',
    'installable': True,
    'application': False,
    'auto_install': False,

    # any module necessary for this one to work correctly
    'depends': ['quality_control'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ]
}
