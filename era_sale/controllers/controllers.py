# -*- coding: utf-8 -*-
# from odoo import http


# class EraSale(http.Controller):
#     @http.route('/era_sale/era_sale/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/era_sale/era_sale/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('era_sale.listing', {
#             'root': '/era_sale/era_sale',
#             'objects': http.request.env['era_sale.era_sale'].search([]),
#         })

#     @http.route('/era_sale/era_sale/objects/<model("era_sale.era_sale"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('era_sale.object', {
#             'object': obj
#         })
