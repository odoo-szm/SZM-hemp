# -*- coding: utf-8 -*-
{
    'name': 'SZM Purchasing Module Enhancement',

    'summary': 'Enhancement to Purchasing Module',

    'description': """
        09-17-20 -  Jeff Mueller, Add Manufacturer attributes to Supplier Info.
        09-30-20 -  Jeff Mueller, Removed Multi-Company requirement from view.
        01-11-21 -  Jeff Mueller, Added Country of Origin.
        02-16-21 -  Jeff Mueller, Various Purchasing Changes.
    """,

    'author': "Precision Solutions, Inc",
    'website': "http://www.precisonline.com",
    "license": "AGPL-3",
    'category': 'Purchasing',
    'sequence': 10,
    'version': '13.0.2.0',
    'installable': True,
    'application': False,
    'auto_install': False,

    # any module necessary for this one to work correctly
    'depends': ['purchase'],

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
