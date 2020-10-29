# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from collections import Counter
from datetime import datetime, date, timedelta
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_compare, float_round

class MrpProductProduce(models.TransientModel):
  _inherit = 'mrp.product.produce'

  lot_id = fields.Many2one('stock.production.lot', string='Lot',required=False)

  # @api.multi
  def do_produce(self):
    self._check_company()
    company = self.env.company
    result = self.env['res.config.settings'].search([],order="id desc", limit=1)
    # Get Day of the year    
#    to_day = datetime.date.today()
     year = datetime.date.today().year
#    day = to_day.toordinal()
#    yearstart = datetime.datetime(to_year,1,1)
#    start = yearstart.toordinal()
#    day_of_year = ((day-start)+1)
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

    company.update({'szm_lotsn' : serial_no})
    lot_serial_no = self.env['stock.production.lot'].create({'name' : lot_no,'product_id':self.product_id.id,'company_id': self.env.company.id})
    print('lot_serial_nooooooooooooooooooooooooooooooooooooooo',lot_serial_no.name)
    self.finished_lot_id = lot_serial_no

    """ Save the current wizard and go back to the MO. """
    # self.ensure_one()
    self._record_production()

    return {
        'type': 'ir.actions.act_window_close'
        }