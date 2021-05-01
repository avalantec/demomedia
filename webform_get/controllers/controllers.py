# -*- coding: utf-8 -*-
# from odoo import http


# class WebformGet(http.Controller):
#     @http.route('/webform_get/webform_get/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/webform_get/webform_get/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('webform_get.listing', {
#             'root': '/webform_get/webform_get',
#             'objects': http.request.env['webform_get.webform_get'].search([]),
#         })

#     @http.route('/webform_get/webform_get/objects/<model("webform_get.webform_get"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('webform_get.object', {
#             'object': obj
#         })
