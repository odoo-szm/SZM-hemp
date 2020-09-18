# -*- coding: utf-8 -*-

from odoo import models, fields, api

class QualityAlert(models.Model):
    _inherit = 'quality.alert'
   
    szm_event = fields.Selection([
        ('EMP NC', 'EMP NC'),
        ('Proc Dev', 'Process Deviation'),
        ('Supp Perf', 'Supplier Performance'),
        ('NC Prod', 'Nonconforming Product'),
        ('NC Srv', 'Nonconforming Service'),
        ('NC Mtl', 'Nonconforming Material'),
        ('Cust Comp', 'Customer Complaint'),
        ('Cust Feed', 'Customer Feedback'),
        ('Imp Opt', 'Improvement Opportunity'),
        ('Doc Mngmt', 'Document Management'),
        ('Other', 'Other')],
        string='Priority', tracking=True, default='none', index=True)
    szm_hold_tag = fields.Char('Hold Tag#')
    szm_prod_rpt_nbr = fields.Char('Product Report#')
    szm_mtl_qty = fields.Integer('Material Affected')
    szm_disposition = fields.Html('Disposition')
    szm_eval_review = fields.Html('Evaluation/Review')
    szm_root_cause = fields.Html('Root Cause Analysis')
    szm_corrective_action = fields.Html('Corrective Action')
