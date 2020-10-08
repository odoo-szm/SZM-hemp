# -*- coding: utf-8 -*-
{
    'name': 'SZM Product Module Enhancement',

    'summary': 'Enhancement to Product Module',

    'description': """
        10-08-20 -  Jeff Mueller, Add Product Attributes for quality.
    """,

    'author': "Precision Solutions, Inc",
    'website': "http://www.precisonline.com",
    "license": "AGPL-3",
    'category': 'Product',
    'sequence': 10,
    'version': '13.0.1.0',
    'installable': True,
    'application': False,
    'auto_install': False,

    # any module necessary for this one to work correctly
    'depends': ['stock'],

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
