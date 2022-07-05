# -*- coding: utf-8 -*-

{
    'name': 'Custom Inventory Changes',

    'summary': 'Inventory Related changes',

    'description': """
        Enhancments to the Odoo stock module for Tenacious Labs.
    """,

    'author': 'Jeff Mueller',
    'website': 'https://www.jrmsyssol.com',

    'category': 'Sales',
    'version': '15.0.0.1',
    'license': 'LGPL-3',
    'depends': ['base', 'stock'],
    'installable': True,
    'auto_install': False,
    'application': False,

    'data': [
      "views/tl_adj_codes.xml",
      "views/stock_quant.xml",
      "security/ir.model.access.csv",
      ],
    'demo': [],
}
