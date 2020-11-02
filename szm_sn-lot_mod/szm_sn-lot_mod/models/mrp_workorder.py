# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from datetime import datetime


class MrpWorkorder(models.Model):
    """ Work Orders """
    _inherit = 'mrp.workorder'

    def _assign_default_final_lot_id(self):
        lot_id_list = self.env['stock.production.lot'].search([('use_next_on_work_order_id', '=', self.id)],
                      order='create_date, id')
        #
        finished_lot = []
        for line in self.finished_workorder_line_ids :
            finished_lot.append(line.lot_id.id)
        #
        for lot in lot_id_list :
            if lot.id in finished_lot :
                continue
            else :
                self.finished_lot_id = lot
                break
        
    def record_production(self):
        res = super(MrpWorkorder, self).record_production()
        #
        if self.qty_produced == self.qty_production :
            for line in self.finished_workorder_line_ids :
                if self.production_id.product_id.tracking == 'serial':
                    line.lot_id.use_next_on_work_order_id = self.next_work_order_id.id
            return res

        if self.production_id.product_id.tracking == 'serial':
            self._assign_default_final_lot_id()
        return res
