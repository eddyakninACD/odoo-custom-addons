{
    'name': 'Factory Management',
    'version': '1.0',
    'category': 'Inventory',
    'summary': 'Manage factory products and suppliers',
    'author': 'Your Name',
    'website': 'https://yourcompany.com',
    'depends': ['base', 'product', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/factory_item_views.xml',
    ],
    'installable': True,
    'application': True,
}

