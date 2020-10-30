class StockMoveLineInherit(models.Model):
    _inherit = 'stock.move.line'

    def action_create_custom_lot_no_szm(self):
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
      company.update({'serial_no' : serial_no})
      if std_lotsn:
        lot_serial_no = self.env['stock.production.lot'].create({'product_id': self.product_id.id,'company_id': self.production_id.company_id.id})
      else:
        lot_serial_no = self.env['stock.production.lot'].create({'name' : lot_no,'product_id':self.product_id.id,'company_id': company.id)
        
      self.lot_name = lot_serial_no
      return
