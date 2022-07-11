# -*- coding: utf-8 -*-

{
    'name': 'Custom Report Templates',

    'summary': 'Customized Report Templates',

    'description': """
        Order/Quotation Form Change to meet Tenacious Labs Requirements
        without impacting standard forms. Company specific form capability.
        BOM Structure changed decimal precision for costs 
    """,

    'author': 'Jeff Mueller',
    'website': 'https://www.jrmsyssol.com',

    'category': 'Sales',
    'version': '15.0.0.4',
    'license': 'LGPL-3',
    'depends': ['base', 'account', 'sale', 'sale_management', 'mrp'],
    'installable': True,
    'auto_install': False,
    'application': False,

    'data': [
        "views/res_company.xml",
        "reports/classic_report_saleorder.xml",
        "reports/custom_report_saleorder.xml",
        "reports/fancy_report_saleorder.xml",
        "reports/modern_report_saleorder.xml",
        "reports/odoo_standard_report_saleorder.xml",
        "reports/tl_report_saleorder.xml",
        # "reports/report_mrp_bom.xml",
        # "reports/report_mrp_bom_line.xml",
             ],
    'demo': [],
}
