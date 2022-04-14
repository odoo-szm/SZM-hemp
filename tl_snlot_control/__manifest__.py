# -*- coding: utf-8 -*-
{
    'name': "tl_snlot_control",

    'summary': """
        Tenacious Labs Lot modification on handling lot numbers at time of receipt and
        when creating a manufacturing order. """,

    'description': """
        Global or Product specific Lot/SN automatic numbering schemes can be
        defined. When a Lot/SN controlled item is received it will automaatically
        create lot number based on lot rules defined for the product.
        When MO is processed the user can automatically create lot number based on 
        lot rules defined for the product. Date method is DDD-YY-NNN, where 
        DDD = Day of the year, YY = Last 2 digits of the year, and NNN = Sequence 
        number of lot.
        03-31-2021 - Changed lot_sn_no return
        04-16-2021 - Moved Lot Counter to Product Template
        04-08-2022 - Upgraded code for version 15.
    """,

    'author'   : "Jeff Mueller",
    'website'  : "http://www.jrmsyssol.com",
    'license'  : 'LGPL-3',
    'category' : 'Manufacturing',
    'version'  : '15.0.1.3',

    # any module necessary for this one to work correctly
    'depends': ['base','mrp','stock'],
    'installable': True,
    'auto_install': False,
    'application': False,
    
    # always loaded
    'data': [
        'views/res_config_setting_views.xml',
        'views/product_template_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}
