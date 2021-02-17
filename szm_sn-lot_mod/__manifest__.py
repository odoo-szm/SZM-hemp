# -*- coding: utf-8 -*-
{
    'name': "szm_sn-lot_mod",

    'summary': """
        SZM Lot modification on handling lot numbers at time of receipt and
        when creating a manufacturing order. """,

    'description': """
        Global or Product specific Lot/SN automatic numbering schemes can be
        defined. When a Lot/SN controlled item is received it will automaatically
        create lot number based on lot rules defined for the product.
        When MO is processed the user can automatically create lot number based on 
        lot rules defined for the product. Date method is DDD-YY-NNN, where 
        DDD = Day of the year, YY = Last 2 digits of the year, and NNN = Sequence 
        number of lot.
    """,

    'author': "Precision Solutions",
    'website': "http://www.precisonline.com",

    'category': 'Manufacturing',
    'version': '13.0.2.0',

    # any module necessary for this one to work correctly
    'depends': ['base','mrp','stock'],
    'installable': True,
    'auto_install': False,
    'application': False,
    
    # always loaded
    'data': [
        # 'views/mrp_product_produce_views.xml',
        'views/res_config_setting_views.xml',
        'views/product_template_views.xml',
        # 'views/stock_move_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}
