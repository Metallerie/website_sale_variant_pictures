# -*- coding: utf-8 -*-

from odoo import models, fields, api



class WesiteSaleVariantPicture(models.Model):
    _inherit = 'product.attribute.value'
    _name = 'product.attribute.value'
    image = fields.Binary('Image', filters='*.png,*.gif,*.jpg,*.jpeg')


# class website_sale_variant_pictures(models.Model):
#     _name = 'website_sale_variant_pictures.website_sale_variant_pictures'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100