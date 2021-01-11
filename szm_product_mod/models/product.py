# -*- coding: utf-8 -*-

from odoo import models, fields, api

# Date        Who             Description
# Jan 11 2020 Jeff Mueller    Added Fields to model

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
    szm_acpt_doc = fields.Html('Acceptance Documentation')
    szm_criteria = fields.Html('Acceptance Criteria')
    
    # Jan 11 2020 Changes
    szm_compose = fields.Text(string='Composition')
    szm_prod_meth = fields.Text(string='Production Method')
    szm_algrn = fields.Boolean('Contains Allergen', help="Contains Allergen Compound")
    szm_gras = fields.Html(string='GRAS')
    szm_coa_per_lot = fields.Boolean('COA per Lot Required', help="COA required per lot")
    szm_spec_req = fields.Text(string='Special Requirements')
    