# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class ProductTemplate(models.Model):
		_inherit = "product.template"

		szm_method_lotsn   = fields.Selection([
				('std', 'Standard'),
				('cust', 'Custom'),
				('date', 'Date')],
				string='Lot/SN Method', default='std')
		szm_digits_lotsn = fields.Integer(string='Digits :')
		szm_prefix_lotsn = fields.Char(string='Prefix :')
		# *04/16/2021 - Added product specific Serial Number
		szm_lotsn = fields.Integer(string='LotSN Counter :')
