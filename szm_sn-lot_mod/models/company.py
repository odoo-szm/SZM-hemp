# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class Company(models.Model):
    _inherit = 'res.company'

    szm_method_lotsn   = fields.Selection([
        ('std', 'Standard'),
        ('cust', 'Custom'),
        ('date', 'Date')],
        string='Lot/SN Method', default='std')
    szm_lotsn = fields.Integer(default = 0)
    szm_digits_lotsn = fields.Integer(string='Digits :')
    szm_prefix_lotsn = fields.Char(string="Prefix :")
