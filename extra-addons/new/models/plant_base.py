from odoo import models, fields

class PlantBase(models.Model):
    _name = 'plant.base'
    _description = '基地表'

    name = fields.Char('基地名称', required=True)
    code = fields.Char('代号', required=True)
    manager_id = fields.Many2one('hr.employee', string='基地经理')
    area = fields.Float('面积(亩)')
