# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class Company(models.Model):
    _inherit = 'res.company'

    szm_lotsn = fields.Integer(default = 0)
    szm_digits_lotsn = fields.Integer(string='Digits :')
    szm_prefix_lotsn = fields.Char(string="Prefix :")
