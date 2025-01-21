# -*- coding: utf-8 -*-
# from odoo import http


# class MaasTrainingOdoo(http.Controller):
#     @http.route('/maas_training_odoo/maas_training_odoo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/maas_training_odoo/maas_training_odoo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('maas_training_odoo.listing', {
#             'root': '/maas_training_odoo/maas_training_odoo',
#             'objects': http.request.env['maas_training_odoo.maas_training_odoo'].search([]),
#         })

#     @http.route('/maas_training_odoo/maas_training_odoo/objects/<model("maas_training_odoo.maas_training_odoo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('maas_training_odoo.object', {
#             'object': obj
#         })

