# -*- coding: utf-8 -*-
# from odoo import http


# class SzmProductMod(http.Controller):
#     @http.route('/szm_product_mod/szm_product_mod/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/szm_product_mod/szm_product_mod/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('szm_product_mod.listing', {
#             'root': '/szm_product_mod/szm_product_mod',
#             'objects': http.request.env['szm_product_mod.szm_product_mod'].search([]),
#         })

#     @http.route('/szm_product_mod/szm_product_mod/objects/<model("szm_product_mod.szm_product_mod"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('szm_product_mod.object', {
#             'object': obj
#         })
