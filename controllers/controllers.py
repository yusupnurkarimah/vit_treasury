# -*- coding: utf-8 -*-
from odoo import http

# class VitTreasury(http.Controller):
#     @http.route('/vit_treasury/vit_treasury/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_treasury/vit_treasury/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_treasury.listing', {
#             'root': '/vit_treasury/vit_treasury',
#             'objects': http.request.env['vit_treasury.vit_treasury'].search([]),
#         })

#     @http.route('/vit_treasury/vit_treasury/objects/<model("vit_treasury.vit_treasury"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_treasury.object', {
#             'object': obj
#         })