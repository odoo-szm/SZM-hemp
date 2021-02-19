# -*- coding: utf-8 -*-

from odoo import models, fields, api

# Date        Who             Description
# Jan 11 2021 Jeff Mueller    Added Country of Origin to model
# Feb 16 2021 Jeff Mueller    Various changes to Purchasing

class SupplierInfo(models.Model):
    _inherit = 'product.supplierinfo'
   
    szm_manf_make = fields.Char('Manufacturer')
    szm_manf_model = fields.Char('Manf. Part Number')
    # Jan 11 2021 Changes
    szm_coo = fields.Many2one('res.country', string='Country of Origin', ondelete='restrict')
    # Feb 16 2021 Changes
    szm_pref_supp = fields.Selection([
      ('Yes', 'Yes'),
      ('Pending', 'Pending'),
      ('No', 'No')], string="Preferred Item/Supplier", help="Preferred Supplier for this item.", default='Yes')

class Partner(models.Model):
    _inherit = 'res.partner'
    
    szm_fda_date = fields.Datetime(string='FDA Dashboard', required=False, index=True, help="FDA Dashboard validated")
    szm_quest_date = fields.Datetime(string='Questionnaire Date', required=False, index=True, help="Date questionairre Last Performed")
    szm_appr_questionnaire = fields.Selection([
      ('Yes', 'Yes'),
      ('Pending', 'Pending'),
      ('No', 'No')], string="Approval Quastionnaire Completed", help="Vendor Approval Questionnaire Completed", default='No', required=True)
    szm_thirdparty_audit = fields.Selection([
      ('Yes', 'Yes'),
      ('Pending', 'Pending'),
      ('No', 'No')], string="3rd Part Audit", help="Third Party Audit on File", default='No', required=True)
    szm_haccp = fields.Selection([
      ('Yes', 'Yes'),
      ('Pending', 'Pending'),
      ('No', 'No')], string="Food Safety/HACCP", help="Food Safety Plan / HACCP", default='No', required=True)
    szm_risk = fields.Selection([
      ('High', 'High'),
      ('Medium', 'Medium'),
      ('Low', 'Low')], string="Risk Rating", help="Risk Rating", default='Low', required=True)
    szm_status = fields.Selection([
      ('Pend', 'Pending'),
      ('Cond', 'Conditional'),
      ('Appr', 'Approved'),
      ('Pref', 'Preferred'),
      ('Emergcy', 'Emergency'),
      ('NA', 'N/A'),
      ('DisQual', 'Disqualified')], string="Supplier Status", help="Supplier Status", default='Pend', required=True)
