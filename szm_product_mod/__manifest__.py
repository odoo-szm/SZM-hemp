# -*- coding: utf-8 -*-
{
    'name': 'SZM Product Module Enhancement',

    'summary': 'Enhancement to Product Module',

    'description': """
        10-08-20 -  Jeff Mueller, Add Product Attributes for quality.
        12-28-20 -  Jeff Mueller, Added Acceptance tab to Product normal view.
        02-16-21 -  Jeff Mueller, Changed various atribute definitions and display criteria
        03-12-21 -  Jeff Mueller, Change Tab for Acceptance and Release Criteria.
    """,

    'author': "Precision Solutions, Inc",
    'website': "http://www.precisonline.com",
    "license": "AGPL-3",
    'category': 'Product',
    'sequence': 10,
    'version': '13.0.2.2',
    'installable': True,
    'application': False,
    'auto_install': False,

    # any module necessary for this one to work correctly
    'depends': ['stock'],

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
