{
    'name': '泰兴项目-批次管理',
    'version': '1.0',
    'category': 'Agriculture',
    'summary': '泰兴公司生产批次信息管理',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/new_model_views.xml',
        'views/plant_batch_views.xml',


    ],
    'installable': True,
    'application': True,
}
