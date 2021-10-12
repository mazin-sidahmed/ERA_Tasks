# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import AccessError, Warning, ValidationError
import warnings


class ProductMinPrice(models.Model):
    _inherit = 'product.template'
    _description = 'Product Minimum Sale Price'

    mini_price = fields.Float(string = 'Minimum Sales Price')

class SaleMinPrice(models.Model):
    _inherit = 'product.pricelist.item'
    _description = 'Product Minimum Sale Price List'

    mini_price = fields.Float(string = 'Minimum Sales Price')

class SaleOrderPriceList(models.Model):
    _inherit = 'sale.order.line'
    _description = 'Sale Order Product Linejnnd'
    
    @api.onchange('price_unit')
    def onchange_price_unit(self):
        for order in self:
            price_list = self.env['product.pricelist.item'].search([])
            for item in price_list:
                if order.product_template_id.name == item.product_id.name:
                    if item.mini_price == 0:
                        product = self.env['product.template'].search([])
                        for rec in product:
                            if order.price_unit < order.product_template_id.list_price and order.price_unit > rec.mini_price:
                                return {'warning':{'title':'Warning','message':'The price is less than sale price'}}

                            if order.price_unit > order.product_template_id.list_price:
                                return {'warning':{'title':'Warning','message':'The price is more than sale price'}}
                    else:
                       
                        if order.price_unit < order.product_template_id.list_price and order.price_unit > item.mini_price:
                            return {'warning':{'title':'Warning','message':'The price is less than sale price'}}

                        if order.price_unit > order.product_template_id.list_price:
                            return {'warning':{'title':'Warning','message':'The price is more than sale price'}}

class SaleOrderPrice(models.Model):
    _inherit = 'sale.order'
    _description = 'Sale Order Product Line'

    @api.constrains('order_line')
    def _unit_price(self):
        for rec in self:
            for price in rec.order_line:
                price_list = self.env['product.pricelist.item'].search([('product_id.name', '=', price.product_template_id.name)])
                for item in price_list:
                    if item.mini_price == 0:
                        product = self.env['product.template'].search([])
                        for rec in product:
                            if price.price_unit < rec.mini_price:
                                raise ValidationError(_("You can’t do that, the price is too low "))
                    else:
                        if price.price_unit < item.mini_price:
                            raise ValidationError(_("You can’t do that, the price is too low "))