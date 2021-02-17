# -*- coding: utf-8 -*-
{
    'name': 'SZM Quality Module Enhancement',

    'summary': 'Enhancement to Quality Alert and Control Points',

    'description': """
        09-17-20 -  Jeff Mueller, Add attributes to QA Module to facilitate
                    tracking of Quality control reporting for GFSI requirements.
        11-19-20 -  Added Selection for disposition, renamed Dispositon Tab to Verification
                    Followup
    """,

    'author': "Precision Solutions, Inc",
    'website': "http://www.precisonline.com",
    "license": "AGPL-3",
    'category': 'Quality',
    'sequence': 10,
    'version': '13.0.2.0',
    'installable': True,
    'application': False,
    'auto_install': False,

    # any module necessary for this one to work correctly
    'depends': ['quality_control'],

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
