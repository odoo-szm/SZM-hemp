# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from datetime import datetime
from odoo.tools import date_utils

# Date        Who             Description
# Mar 31 2021 Jeff Mueller    Removed standard lot generation statement
# Apr 16 2021 Jeff Mueller    Move LotSN from Company to Product

class MrpProductionInherit(models.Model):
    """ Manufacturing Orders """
    _inherit = 'mrp.production'

    def create_custom_lot_no(self,wo):
        # company = self.env.company
        result = self.env['res.config.settings'].search([],order="id desc", limit=1)
        # Get Day of the year    
        year = fields.Date.today().year
        day_of_year = datetime.today().timetuple().tm_yday
        std_lotsn = False
        digit = 9
        prefix = ''
        # DOY Padding
        doy_digits = len(str(day_of_year))
        diffrence = abs(doy_digits - 3)
        if diffrence > 0:
            doy_pad = "0"
            for i in range(diffrence-1) :
              doy_pad = doy_pad + "0"
        else :
            doy_pad = ""
      
        string_doy = doy_pad + str(day_of_year)
  
        if result.szm_apply_method == "global":
            if result.szm_method_lotsn == "cust":
              digit = result.szm_digits_lotsn
              prefix = result.szm_prefix_lotsn
            elif result.szm_method_lotsn == "date":
              """ Form Settings Date based Lot/SN """
              digit  = 3
              prefix = string_doy + "-" + str(year)[-2:] + "-"
            else:
              std_lotsn = True
        else:
            if self.product_id.szm_method_lotsn == "cust":
              digit = self.product_id.szm_digits_lotsn
              prefix = self.product_id.szm_prefix_lotsn
            elif self.product_id.szm_method_lotsn == "date":
              """ Form Product Date based Lot/SN """
              digit  = 3
              prefix = string_doy + "-" + str(year)[-2:] + "-"
            else:
              std_lotsn = True
          
        serial_no = self.product_id.szm_lotsn + 1
        serial_no_digit=len(str(self.product_id.szm_lotsn))

        # diffrence = abs(serial_no_digit - digit)
        diffrence = (digit - serial_no_digit)

        if diffrence > 0:
          sn_pad = "0"
          for i in range(diffrence-1) :
            sn_pad = sn_pad + "0"
        else :
          sn_pad = ""

        if prefix != False:
          temp = str(serial_no)[-digit:]
          lot_no = prefix + sn_pad + temp
        else:
          lot_no = str(serial_no)

        self.product_id.update({'szm_lotsn' : serial_no})
        if std_lotsn:
          lot_serial_no = self.env['stock.production.lot'].create({'name' : lot_no,'product_id':self.product_id.id,'company_id': company.id,'use_next_on_work_order_id' : wo.id})
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