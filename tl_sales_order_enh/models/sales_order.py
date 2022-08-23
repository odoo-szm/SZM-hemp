# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

# Date        Who             Description
# Aug 23 2022 Jeff Mueller    Changed order of selection in compute_delivery_status


class SalesOrder(models.Model):
    _inherit = 'sale.order'

    tl_delivery_status = fields.Selection(selection=[
        ('nothing', 'Nothing to Deliver'), ('to_deliver', 'To Deliver'),
        ('partial', 'Partially Deliver'), ('delivered', 'Delivered'),
        ('processing', 'Processing')], string='Delivery Status', compute='_compute_delivery_status', store=True,
        readonly=True, copy=False, default='nothing')

    @api.depends('state', 'order_line.qty_delivered')
    def _compute_delivery_status(self):
        for rec in self:
            pickings = self.env['stock.picking'].search([('sale_id', '=', rec.id)])
            orderlines = rec.mapped('order_line')
            if all(oline.qty_delivered == 0 for oline in orderlines):
                rec.tl_delivery_status = 'to_deliver'
            elif orderlines.filtered(lambda x: x.qty_delivered < x.product_uom_qty):
                rec.tl_delivery_status = 'partial'
            elif all(oline.qty_delivered == oline.product_uom_qty for oline in orderlines):
                rec.tl_delivery_status = 'delivered'
            elif any(pick.state in ('waiting', 'confirmed') for pick in pickings):
                rec.tl_delivery_status = 'processing'
            elif not pickings:
                rec.tl_delivery_status = 'nothing'
