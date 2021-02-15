# -*- coding: utf-8 -*-

from odoo import models, fields, api

# Date        Who             Description
# Jan 11 2021 Jeff Mueller    Added Fields to model
# Feb 16 2021 Jeff Mueller    Changed various atribute definitions and display criteria

class Product(models.Model):
    _inherit = 'product.template'

    szm_manf_specs = fields.Selection([
      ('Yes', 'Yes'),
      ('NA', 'N/A'),
      ('No', 'No')], string="Manf Spec on File", help="Manufacturers Specifications on File", default='NA', required=True)
    szm_risk = fields.Selection([
      ('High', 'High'),
      ('Medium', 'Medium'),
      ('Low', 'Low')], string="Risk Rating", help="Risk Rating", default='Low', required=True)
    szm_coa_file = fields.Boolean('Sample CoA on File', help="If checked, Sample CoA is on File.")
    szm_algrn_stmt = fields.Boolean('Allergen Statement', help="Allergen Statement Required")
    szm_coo = fields.Many2one('res.country', string='Country of Origin', ondelete='restrict')
    szm_acpt_doc = fields.Html('Release Documentation')
    szm_criteria = fields.Html('Release Criteria')
    
    # Jan 11 2021 Changes
    szm_compose = fields.Text(string='Composition')
    szm_prod_meth = fields.Text(string='Production Method')
    szm_algrn = fields.Boolean('Contains Allergen', help="Contains Allergen Compound")
    szm_gras = fields.Boolean('GRAS', help="G.R.A.S.")
    szm_coa_per_lot = fields.Boolean('COA per Lot Required', help="COA required per lot")
    szm_spec_req = fields.Text(string='Special Requirements')

    # Feb 16 2021 Changes
    szm_int_desc = fields.Text(string='Product Description')