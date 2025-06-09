{
    'name': 'New',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Odoo 18 最简自定义模块测试',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/new_model_views.xml',

    ],
    'installable': True,
    'application': True,
}
