from odoo import models, fields, api

class FactoryItem(models.Model):
    _name = 'factory.item'
    _description = 'Factory Item'

    # Identification Fields
    item_code = fields.Char(string='Item Code', required=True, index=True)
    reference_code = fields.Char(string='Reference Code')
    barcode = fields.Char(string='Barcode')

    # Category & Classification
    product_category_id = fields.Many2one('product.category', string='Product Category', required=True)
    is_storable = fields.Boolean(string='Track Inventory', default=True)
    is_service = fields.Boolean(string='Is Service?', default=False)
    is_packaging = fields.Boolean(string='Is Packaging?', default=False)
    is_kashrut = fields.Boolean(string='Kosher Certified?')
    is_passover_kosher = fields.Selection([
        ('yes', 'Yes'), ('leaven', 'Leaven'), ('no', 'No')
    ], string='Passover Kosher')

    # Vendor & Supplier Management
    supplier_id = fields.Many2one('res.partner', string='Primary Vendor', domain=[('supplier_rank', '>', 0)])
    vendor_price = fields.Float(string='Supplier Price')
    vendor_commission = fields.Float(string='Supplier Commission (%)')

    # Sales & POS Configuration
    sale_price = fields.Float(string='Sale Price', required=True)
    available_in_pos = fields.Boolean(string='Available in POS?', default=True)
    is_wholesale = fields.Boolean(string='Can Be Sold Wholesale?')
    min_sale_qty = fields.Float(string='Min Sale Quantity', default=1.0)
    max_sale_qty = fields.Float(string='Max Sale Quantity', help='Maximum quantity allowed per sale')

    # Logistics & UoM
    uom_id = fields.Many2one('uom.uom', string='Unit of Measure', required=True)
    uom_po_id = fields.Many2one('uom.uom', string='Purchase UoM', required=True)
    packaging_type = fields.Selection([
        ('pallet', 'Pallet'),
        ('cardboard', 'Cardboard Box'),
        ('plastic', 'Plastic Container'),
        ('bag', 'Bag'),
        ('other', 'Other')
    ], string='Packaging Type')

    # Country of Origin & Attributes
    country_of_origin = fields.Many2one('res.country', string='Country of Origin')
    content_uom = fields.Selection([
        ('kg', 'Kilogram'), ('liter', 'Liter'), ('unit', 'Unit')
    ], string='Content UOM')

    # Regulatory & Restrictions
    is_alcohol = fields.Boolean(string='Contains Alcohol?')
    is_age_restricted = fields.Boolean(string='Age Restricted?')
    is_no_return_pos = fields.Boolean(string='No Return on POS?')
    is_price_transparency = fields.Boolean(string='Price Transparency Site Export?')

    # Inventory Tracking
    track_lot = fields.Boolean(string='Track Lot/Serial Numbers?')
    stock_quantity = fields.Float(string='Stock Quantity')

    # Tax & Costing
    cost_price = fields.Float(string='Cost Price')
    sale_tax = fields.Many2one('account.tax', string='Sale Tax')
    cost_tax = fields.Many2one('account.tax', string='Cost Tax')

    # Status & System Fields
    is_active = fields.Boolean(string='Active', default=True)
    product_status = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('archived', 'Archived')
    ], string='Product Status', default='draft')

