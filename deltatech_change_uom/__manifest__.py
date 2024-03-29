# ©  2008-2021 Deltatech
#              Dorin Hongu <dhongu(@)gmail(.)com
# See README.rst file on addons root folder for license details

{
    'name': 'Change Unit of measure',
    'summary': 'Change unit of measure in product',
    'version': '15.0.1.0.0',
    'author': 'Terrabit, Dorin Hongu',
    'website': 'https://www.terrabit.ro',
    'category': 'Accounting',
    'depends': ['product', 'account', 'stock', 'sale_management', 'purchase'],
    'installable': True,
    'license': 'LGPL-3',
    'auto_install': False,
    'application': False,
    'data': [
        'security/sale_security.xml',
        'wizard/product_change_uom_view.xml',
        'security/ir.model.access.csv',
    ],
    'images': ['static/description/main_screenshot.png'],
    'development_status': 'Beta',
    'maintainers': ['dhongu'],
}