# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class res_company(models.Model):
    _inherit = "res.company"

    sale_template = fields.Selection([
            ('fancy', 'Fancy'),
            ('classic', 'Classic'),
            ('modern', 'Modern'),
            ('odoo_standard', 'Odoo Standard'),
        ], 'Sale')

class res_company(models.Model):
    _inherit = "res.company"

    bank_account_id = fields.Many2one('res.partner.bank', 'Bank Account')

class res_partner_bank(models.Model):
    _inherit = "res.partner.bank"

    street = fields.Char('Street')
    street2 = fields.Char('Street2')
    zip = fields.Char('Zip', size=24, change_default=True)
    city = fields.Char('City')
    state_id = fields.Many2one("res.country.state", 'State')
    country_id = fields.Many2one('res.country', 'Country')
    swift_code = fields.Char('Swift Code')
    ifsc = fields.Char('IFSC')
    branch_name = fields.Char('Branch Name')


class sale_order(models.Model):
    _inherit = 'sale.order'

    def print_quotation(self):
        self.filtered(lambda s: s.state == 'draft').write({'state': 'sent'})
        return self.env.ref('tl_custom_reports.custom_report_sale_order').report_action(self)