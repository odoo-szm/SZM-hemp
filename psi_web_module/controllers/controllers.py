# -*- coding: utf-8 -*-
from odoo import http


class PsiWebModule(http.Controller):
    @http.route('/helloworld', auth='public', website=True)
    def helloworld(self, **kwargs):
        return request.render('helloworld.hello')

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
