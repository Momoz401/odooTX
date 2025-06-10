from odoo import models, fields

class PlantBatch(models.Model):
    _name = 'plant.batch'
    _description = '批次表'
    name = fields.Char('批次编号', required=True)
    category = fields.Char('类别')  # 可以改成 Many2one 关联类别表
    area = fields.Float('面积(亩)')
    start_date = fields.Date('种植日期')
    end_date = fields.Date('采收期末')
    manager_id = fields.Char('基地经理')  # 建议后续做成 Many2one 关联员工表
    remark = fields.Text('备注')