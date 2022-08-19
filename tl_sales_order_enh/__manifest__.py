# -*- coding: utf-8 -*-
{
    'name': 'Tenacious Labs Order Enhancements',

    'summary': 'Enhancements to Sales Order',

    'description': """
        Compilation of Sales module enhancements.
        Visibility of a sales order ship status (complements of Cybrosys.
        10-06-21 -  Cybrosys Technologies Pvt. Ltd., sales Delivery Status.
    """,

    'author': "JRM Business Systems Solutions, LLC & Cybrosys Techno Solutions",
    'website': "http://www.jrmsyssol.com",
    "license": "LGPL-3",
    'category': 'Sales',
    'sequence': 13,
    'version': '15.0.1.0',
    'installable': True,
    'application': False,
    'auto_install': False,

    # any module necessary for this one to work correctly
    'depends': ['sale_management', 'stock', 'mrp'],

    # always loaded
    'data': [
        'views/sales_order.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ]
}