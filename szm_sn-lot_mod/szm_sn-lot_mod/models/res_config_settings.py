# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class ResConfigSettings(models.TransientModel):
	_inherit = 'res.config.settings'

	szm_digits_lotsn = fields.Integer(string='Digits :',related="company_id.digits_serial_no",readonly=False)
	szm_prefix_lotsn = fields.Char(string="Prefix :",related="company_id.prefix_serial_no",readonly=False)
	szm_apply_method = fields.Selection([("global","Global"),("product",'Product Level')],'Lot/SN Application Method',default="product")

	@api.model
	def get_values(self):
		res = super(ResConfigSettings, self).get_values()
		res.update(apply_method = self.env['ir.config_parameter'].sudo().get_param('szm_sn-lot_mod.szm_apply_method'))
		return res

	# @api.multi
	def set_values(self):
		super(ResConfigSettings, self).set_values()
		self.env['ir.config_parameter'].sudo().set_param('szm_sn-lot_mod.szm_apply_method', self.szm_apply_method)
