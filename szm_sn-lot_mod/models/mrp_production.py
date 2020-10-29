# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from datetime import datetime

class MrpProductionInherit(models.Model):
    """ Manufacturing Orders """
    _inherit = 'mrp.production'

    def create_custom_lot_no(self,wo):
        company = self.env.company
        result = self.env['res.config.settings'].search([],order="id desc", limit=1)
#       to_day = datetime.date.today()
        year = datetime.date.today().year
#       day = to_day.toordinal()
#       yearstart = datetime.datetime(to_year,1,1)
#       start = yearstart.toordinal()
#       day_of_year = ((day-start)+1)
        day_of_year = date.fromordinal(date(year, 1, 1).toordinal() + days - 1
        std_lotsn = False
      
        if result.szm_apply_method == "global":
            if result.szm_method_lotsn == "cust":
              digit = result.szm_digits_lotsn
              prefix = result.szm_prefix_lotsn
            else:
              """ Form Settings Date based Lot/SN """
              if result.szm_method_lotsn == "date":
                digit  = 2
                prefix = "T" + day_of_year + "-" + year + "-"
              else:
                std_lotsn = True
        else:
            if self.product_id.szm_method_lotsn == "cust":
              digit = self.product_id.szm_digits_lotsn
              prefix = self.product_id.szm_prefix_lotsn
            else:
              """ Form Product Date based Lot/SN """
              if self.product_id.szm_method_lotsn == "date":
                digit  = 2
                prefix = "T" + day_of_year + "-" + year + "-"
              else:
                std_lotsn = True
              
        serial_no = company.szm_lotsn + 1
        serial_no_digit=len(str(company.szm_lotsn))

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
        if std_lotsn:
          lot_serial_no = self.env['stock.production.lot'].create({'product_id': self.product_id.id,'company_id': self.production_id.company_id.id})
        else:
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
