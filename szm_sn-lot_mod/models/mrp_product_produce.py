# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from collections import Counter
from datetime import datetime, date, timedelta
from odoo.addons import decimal_precision as dp
# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from collections import Counter
from datetime import datetime, date, timedelta
from odoo.tools import date_utils
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_compare, float_round

class MrpProductProduce(models.TransientModel):
  _inherit = 'mrp.product.produce'

  lot_id = fields.Many2one('stock.production.lot', string='Lot',required=False)

  # @api.multi
  def do_produce(self):
    if self.finished_lot_id == '':      
      self.finished_lot_id = self._get_lotsn_szm

    """ Save the current wizard and go back to the MO. """
    # self.ensure_one()
    self._record_production()

    return {
        'type': 'ir.actions.act_window_close'
        }
        
  def action_generate_serial(self):
    self.ensure_one()
    product_produce_wiz = self.env.ref('mrp.view_mrp_product_produce_wizard', False)
    self.finished_lot_id = self._get_lotsn_szm
#    self.finished_lot_id = self.env['stock.production.lot'].create({
#        'product_id': self.product_id.id,
#        'company_id': self.production_id.company_id.id
#    })
    return {
        'name': _('Produce'),
        'type': 'ir.actions.act_window',
        'view_mode': 'form',
        'res_model': 'mrp.product.produce',
        'res_id': self.id,
        'view_id': product_produce_wiz.id,
        'target': 'new',
    }

  def _get_lotsn_szm(self):
    self._check_company()
    company = self.env.company
    result = self.env['res.config.settings'].search([],order="id desc", limit=1)

    # Get Day of the year    
    year = fields.Date.today().year
    day_of_year = datetime.today().timetuple().tm_yday
    std_lotsn = False
    digit = 9
    prefix = ''
  
    if result.szm_apply_method == "global":
        if result.szm_method_lotsn == "cust":
          digit = result.szm_digits_lotsn
          prefix = result.szm_prefix_lotsn
        elif result.szm_method_lotsn == "date":
          """ Form Settings Date based Lot/SN """
          digit  = 2
          prefix = str(day_of_year) + "-" + str(year)[-2:] + "-"
        else:
          std_lotsn = True
    else:
        if self.product_id.szm_method_lotsn == "cust":
          digit = self.product_id.szm_digits_lotsn
          prefix = self.product_id.szm_prefix_lotsn
        elif self.product_id.szm_method_lotsn == "date":
          """ Form Product Date based Lot/SN """
          digit  = 2
          prefix = str(day_of_year) + "-" + str(year)[-2:] + "-"
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
    if std_lotsn:
      lot_serial_no = self.env['stock.production.lot'].create({'product_id': self.product_id.id,'company_id': self.production_id.company_id.id})
    else:
      lot_serial_no = self.env['stock.production.lot'].create({'name' : lot_no,'product_id':self.product_id.id,'company_id': self.env.company.id})

    print('lot_serial_nooooooooooooooooooooooooooooooooooooooo',lot_serial_no.name)

    return lot_serial_no
