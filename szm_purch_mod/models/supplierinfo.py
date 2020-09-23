# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SupplierInfo(models.Model):
    _inherit = 'product.supplierinfo'
   
    szm_manf_make = fields.Char('Manufacturer')
    szm_manf_model = fields.Char('Manf. Part Number')

class Partner((models.Model):
    _inherit = 'res.partner'
    
    szm_fda_dashboard = fields.Selection([
      ('Yes', 'Yes'),
      ('Pending', 'Pending'),
      ('No', 'No')], string="FDA Dashboard", help="FDA Dashboard /FTC Validated", default='No', required=True)
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
      ('Low', 'Low')], string="Risk Rating", help="Risk Rating", default='High', required=True)
    szm_status = fields.Selection([
      ('Pend', 'Pending'),
      ('Cond', 'Conditional'),
      ('Appr', 'Approved'),
      ('Emergcy', 'Emergency'),
      ('DisQual', 'Disqualified')], string="Status", help="Supplier Status", default='Pend', required=True)
