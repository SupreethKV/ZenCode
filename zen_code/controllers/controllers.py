# -*- coding: utf-8 -*-
from odoo import http

# class ZeeCode(http.Controller):
#     @http.route('/zee_code/zee_code/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/zee_code/zee_code/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('zee_code.listing', {
#             'root': '/zee_code/zee_code',
#             'objects': http.request.env['zee_code.zee_code'].search([]),
#         })

#     @http.route('/zee_code/zee_code/objects/<model("zee_code.zee_code"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('zee_code.object', {
#             'object': obj
#         })