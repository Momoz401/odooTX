# models/product_template_inherit.py

from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    secondary_category = fields.Char(string='Secondary Category')