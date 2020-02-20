# -*- coding: utf-8 -*-
# from odoo import http


# class Modelo2(http.Controller):
#     @http.route('/modelo2/modelo2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modelo2/modelo2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modelo2.listing', {
#             'root': '/modelo2/modelo2',
#             'objects': http.request.env['modelo2.modelo2'].search([]),
#         })

#     @http.route('/modelo2/modelo2/objects/<model("modelo2.modelo2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modelo2.object', {
#             'object': obj
#         })
