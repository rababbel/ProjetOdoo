# -*- coding: utf-8 -*-
# from odoo import http


# class Feedbacks(http.Controller):
#     @http.route('/feedbacks/feedbacks/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/feedbacks/feedbacks/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('feedbacks.listing', {
#             'root': '/feedbacks/feedbacks',
#             'objects': http.request.env['feedbacks.feedbacks'].search([]),
#         })

#     @http.route('/feedbacks/feedbacks/objects/<model("feedbacks.feedbacks"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('feedbacks.object', {
#             'object': obj
#         })
