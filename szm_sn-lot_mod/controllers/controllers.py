# -*- coding: utf-8 -*-
# from odoo import http


# class SzmSn-lotMod(http.Controller):
#     @http.route('/szm_sn-lot_mod/szm_sn-lot_mod/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/szm_sn-lot_mod/szm_sn-lot_mod/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('szm_sn-lot_mod.listing', {
#             'root': '/szm_sn-lot_mod/szm_sn-lot_mod',
#             'objects': http.request.env['szm_sn-lot_mod.szm_sn-lot_mod'].search([]),
#         })

#     @http.route('/szm_sn-lot_mod/szm_sn-lot_mod/objects/<model("szm_sn-lot_mod.szm_sn-lot_mod"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('szm_sn-lot_mod.object', {
#             'object': obj
#         })
