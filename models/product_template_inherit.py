from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    discount_limit = fields.Float(string='Discount Limit %', default=0.0)

    @api.constrains('discount_limit')
    def _check_discount_limit(self):
        for rec in self:
            if rec.discount_limit < 0 or rec.discount_limit > 100:
                raise ValidationError('Discount limit must be between 0 and 100')


