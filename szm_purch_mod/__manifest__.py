# -*- coding: utf-8 -*-
{
    'name': 'SZM Purchasing Module Enhancement',

    'summary': 'Enhancement to Purchasing Module',

    'description': """
        09-17-20 -  Jeff Mueller, Add Manufacturer attributes to Supplier Info.
    """,

    'author': "Precision Solutions, Inc",
    'website': "http://www.precisonline.com",
    "license": "AGPL-3",
    'category': 'Purchasing',
    'sequence': 10,
    'version': '13.0.1.0',
    'installable': True,
    'application': False,
    'auto_install': False,

    # any module necessary for this one to work correctly
    'depends': ['Purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ]
}
