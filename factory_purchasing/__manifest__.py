{
    'name': 'Factory Purchasing',
    'version': '1.0',
    'summary': 'Manage factory purchasing items',
    'description': 'Module for factory purchasing department to handle item management.',
    'category': 'Purchases',
    'author': 'Your Name',
    'website': 'https://yourcompany.com',
    'depends': ['base', 'purchase'],
    'data': [
        'security/ir.model.access.csv',
        'views/factory_item_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
