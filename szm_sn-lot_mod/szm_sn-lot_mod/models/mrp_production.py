# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class MrpProductionInherit(models.Model):
    """ Manufacturing Orders """
    _inherit = 'mrp.production'

    def create_custom_lot_no(self,wo):
        company = self.env.company
        result = self.env['res.config.settings'].search([],order="id desc", limit=1)

        if result.apply_method == "global":
            digit = result.digits_serial_no
            prefix = result.prefix_serial_no
        else:
            digit = self.product_id.digits_serial_no
            prefix = self.product_id.prefix_serial_no
            
        serial_no = company.serial_no + 1
        serial_no_digit=len(str(company.serial_no))

        diffrence = abs(serial_no_digit - digit)
        if diffrence > 0:
            no = "0"
            for i in range(diffrence-1) :
                no = no + "0"
        else :
            no = ""

        if prefix != False:
            lot_no = prefix+no+str(serial_no)
        else:
            lot_no = str(serial_no)
        company.update({'serial_no' : serial_no})
        lot_serial_no = self.env['stock.production.lot'].create({'name' : lot_no,'product_id':self.product_id.id,'company_id': company.id,'use_next_on_work_order_id' : wo.id})
        return lot_serial_no

    def _workorders_create(self, bom, bom_data):

        res = super(MrpProductionInherit, self)._workorders_create(bom,bom_data)
        if self.product_id.tracking == 'serial' :
            lot_id_list = []
            for i in range(0,int(self.product_qty)) :
                lot_id = self.create_custom_lot_no(res[0])
                lot_id_list.append(lot_id.id)
            res[0].finished_lot_id = lot_id_list[0]

        elif self.product_id.tracking == 'lot' :
            lot_id = self.create_custom_lot_no(res[0])
            for lot in res:
                lot.finished_lot_id = lot_id.id
        return res