# -*- coding: utf-8 -*-
from odoo import http

# class WebsiteSaleVariantPictures(http.Controller):
#     @http.route('/website_sale_variant_pictures/website_sale_variant_pictures/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_sale_variant_pictures/website_sale_variant_pictures/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_sale_variant_pictures.listing', {
#             'root': '/website_sale_variant_pictures/website_sale_variant_pictures',
#             'objects': http.request.env['website_sale_variant_pictures.website_sale_variant_pictures'].search([]),
#         })

#     @http.route('/website_sale_variant_pictures/website_sale_variant_pictures/objects/<model("website_sale_variant_pictures.website_sale_variant_pictures"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_sale_variant_pictures.object', {
#             'object': obj
#         })