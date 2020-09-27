# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SupplierInfo(models.Model):
    _inherit = 'product.supplierinfo'
   
    szm_manf_make = fields.Char('Manufacturer')
    szm_manf_model = fields.Char('Manf. Part Number')