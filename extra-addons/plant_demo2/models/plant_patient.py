from odoo import models, fields

class PlantPatient(models.Model):
    _name = 'plant.patient'
    _description = 'Plant Patient 测试表'

    name = fields.Char(string='作物名', required=True)
    age = fields.Integer(string='作物龄')
    note = fields.Text(string='备注')