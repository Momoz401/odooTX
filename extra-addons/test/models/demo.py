from odoo import models, fields

class TestDemo(models.Model):
    _name = 'test.demo'
    _description = '测试记录'

    name = fields.Char('名称', required=True)
    desc = fields.Text('描述')