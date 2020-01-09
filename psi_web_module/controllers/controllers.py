# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class PsiWebModule(http.Controller):
    @http.route('/hello', auth='public', website=True)
    def index(self, **kw):
        return request.render('SZM-hemp.hello')

# class PsiWebModule(http.Controller):
#     @http.route('/psi_web_module/psi_web_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/psi_web_module/psi_web_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('psi_web_module.listing', {
#             'root': '/psi_web_module/psi_web_module',
#             'objects': http.request.env['psi_web_module.psi_web_module'].search([]),
#         })

#     @http.route('/psi_web_module/psi_web_module/objects/<model("psi_web_module.psi_web_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('psi_web_module.object', {
#             'object': obj
#         })
