from odoo import models, fields

class FactoryItem(models.Model):
    _name = 'factory.item'
    _description = 'Factory Item'

    item_code = fields.Char(string="Item Code", index=True)
    item_name = fields.Char(string='Item Name', required=True)
    category_id = fields.Many2one('product.category', string='Category')
    supplier_id = fields.Many2one('res.partner', string='Supplier', domain=[('supplier_rank', '>', 0)])
    purchase_price = fields.Float(string='Purchase Price')
    uom_id = fields.Many2one('uom.uom', string='Unit of Measure')
    stock_quantity = fields.Float(string='Stock Quantity')
    active = fields.Boolean(string='Active', default=True)

    from odoo import models, fields

class FactoryItem(models.Model):
    _name = 'factory.item'  # The model name
    _description = 'Factory Item'

    item_code = fields.Char(string="Item Code", index=True, required=True)

    _sql_constraints = [
        ('unique_item_code', 'unique(item_code)', 'Item Code must be unique!')
    ]

