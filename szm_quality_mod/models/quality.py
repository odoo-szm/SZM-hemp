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
        ('Recall', 'Withdrawal/Recall'),
        ('Other', 'Other')],
        string='Event', tracking=True, default='Other')
    szm_dispose = fields.Selection([
        ('rewrk', 'Rework'),
        ('dstry', 'Destroyed'),
        ('uai', 'Use As Is'),
        ('rts', 'Return to Supplier'),
        ('na', 'N/A')],
        string='Disposition', tracking=True)
    szm_hold_tag = fields.Char('Hold Tag#')
    szm_prod_rpt_nbr = fields.Char('Product Report#')
    szm_mtl_qty = fields.Integer('Material Affected')
    szm_disposition = fields.Html('Verification/Followup')
    szm_disposition_date = fields.Datetime(string='Disposition Date', required=False, index=True, help="Date Dispositon Completed")
    szm_eval_review = fields.Html('Evaluation/Review')
    szm_eval_date = fields.Datetime(string='Evaluation Date', required=False, index=True, help="Date Evaluation Completed")
    szm_root_cause = fields.Html('Root Cause Analysis')
    szm_rc_date = fields.Datetime(string='Root Cause Date', required=False, index=True, help="Date Root Cause Completed")
    szm_ca_date = fields.Datetime(string='Corrective Action Date', required=False, index=True, help="Corrective Action Completed")
