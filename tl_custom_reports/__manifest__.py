# -*- coding: utf-8 -*-

{
    'name': 'Custom Report Templates',

    'summary': 'Customized Report Template for Quotation/SO/Sales',

    'description': """
		    Customize report, customize pdf report, customize template report, Customize Sales Order report,
        Customize Purchase Order report, Customize invoice report, Customize delivery Order report
    """,

    'author': 'Jeff Mueller',
    'website': 'https://www.jrmsyssol.com',

    'category': 'Sales',
    'version': '15.0.0.2',
    'license': 'LGPL-3',
    'depends': ['base', 'account', 'sale', 'sale_management'],
    'installable': True,
    'auto_install': False,
    'application': False,

    'data': [
        "views/res_company.xml",
        "reports/classic_report_saleorder.xml",
        "reports/fancy_report_saleorder.xml",
        "reports/modern_report_saleorder.xml",
        "reports/odoo_standard_report_saleorder.xml",
             ],
    'demo': [],
}
