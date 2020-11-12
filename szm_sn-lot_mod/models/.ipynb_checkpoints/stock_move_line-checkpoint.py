# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from datetime import datetime
from odoo.tools import date_utils

class StockMoveLineInherit(models.Model):
    _inherit = 'stock.move.line'
        
    @api.onchange('lot_name', 'lot_id')
    def onchange_serial_number(self):
      super(StockMoveLineInherit, self).onchange_serial_number()
      if not self.lot_name:
        self._get_lotsn_szm()
    
    def _get_lotsn_szm(self):
      company = self.env.company
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
            
      serial_no = company.szm_lotsn + 1
      serial_no_digit=len(str(company.szm_lotsn))
      # Determine SN Padding
      diffrence = abs(serial_no_digit - digit)
      if diffrence > 0:
          sn_pad = "0"
          for i in range(diffrence-1) :
              sn_pad = sn_pad + "0"
      else :
          sn_pad = ""
      

      if prefix != False:
          lot_no = prefix+sn_pad+str(serial_no)
      else:
          lot_no = str(serial_no)
      
      company.update({'szm_lotsn' : serial_no})
        
      self.lot_name = lot_no
      return