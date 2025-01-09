# -*- coding: utf-8 -*-
# from odoo import http


# class DrdSchoolManagement(http.Controller):
#     @http.route('/drd_school_management/drd_school_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/drd_school_management/drd_school_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('drd_school_management.listing', {
#             'root': '/drd_school_management/drd_school_management',
#             'objects': http.request.env['drd_school_management.drd_school_management'].search([]),
#         })

#     @http.route('/drd_school_management/drd_school_management/objects/<model("drd_school_management.drd_school_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('drd_school_management.object', {
#             'object': obj
#         })

