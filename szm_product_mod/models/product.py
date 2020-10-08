# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Product(models.Model):
    _inherit = 'product.template'

    szm_manf_specs = fields.Selection([
      ('Yes', 'Yes'),
      ('NA', 'N/A'),
      ('No', 'No')], string="Manf Spec on File", help="Manufacturers Specifications on File", default='NA', required=True)
    szm_risk = fields.Selection([
      ('High', 'High'),
      ('Medium', 'Medium'),
      ('Low', 'Low')], string="Risk Rating", help="Risk Rating", default='High', required=True)
    szm_coa_file = fields.Boolean('Sample CoA on File', help="If checked, Sample CoA is on File.")
    szm_algrn_stmt = fields.Boolean('Allergen Statement', help="Allergen Statement Required")
    szm_coo = fields.Many2one('res.country', string='Country of Origin', ondelete='restrict')