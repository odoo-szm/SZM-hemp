# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class TLAdjustmentCode(models.Model):
    _name = 'tl.adj.codes'
    _description = 'Inventory Adjustment Codes'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')

class StockQuant(models.Model):
    _inherit = "stock.quant"

    tl_adj_reas_id = fields.Many2one(
        'tl.adj.codes', 'Adjustment Code',
        required=False, help="Select adjustment reason.")

