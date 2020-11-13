# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class ProductTemplate(models.Model):
    _inherit = "product.template"

    szm_digits_lotsn = fields.Integer(string='Digits :')
    szm_prefix_lotsn = fields.Char(string="Prefix :")
