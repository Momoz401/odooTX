
print("✅ PlantBatch 模型被加载！")
from odoo import models, fields, api
from datetime import timedelta

class PlantBatch(models.Model):
    _name = 'plant.batch'
    _description = '种植批次'

    name = fields.Char(string='批次ID', required=True)
    base_manager = fields.Char(string='基地经理')
    plot = fields.Char(string='地块')
    area = fields.Float(string='面积（亩）')
    plant_date = fields.Date(string='种植日期')
    grow_cycle = fields.Integer(string='生长周期（天）')
    harvest_cycle = fields.Integer(string='采收周期（天）')
    harvest_start = fields.Date(string='采收初期', compute='_compute_dates', store=True)
    harvest_end = fields.Date(string='采收末期', compute='_compute_dates', store=True)
    note = fields.Text(string='备注')

    @api.depends('plant_date', 'grow_cycle', 'harvest_cycle')
    def _compute_dates(self):
        for rec in self:
            if rec.plant_date and rec.grow_cycle:
                rec.harvest_start = rec.plant_date + timedelta(days=rec.grow_cycle)
                rec.harvest_end = rec.harvest_start + timedelta(days=rec.harvest_cycle or 0)
            else:
                rec.harvest_start = rec.harvest_end = False