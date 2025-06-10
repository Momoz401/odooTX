from odoo import models, fields, api

class PlantBatch(models.Model):
    _name = 'plant.batch'
    _description = '批次表'

    name = fields.Char('批次编号', required=True, readonly=True, copy=False)
    area = fields.Float('面积(亩)')
    start_date = fields.Date('种植日期', required=True)
    end_date = fields.Date('采收期末')
    manager_id = fields.Many2one(
        'hr.employee',
        string='基地经理',
        domain="[('job_title','=','基地经理')]",
        required=True
    )
    base_code = fields.Char(
        string='基地代号',
        related='manager_id.base_code',
        store=True,
        readonly=True
    )
    product_id = fields.Many2one(
        'product.product',
        string='产品名称',
        required=True
    )
    remark = fields.Text('备注')

    @api.model
    def create(self, vals):
        date_str = ''
        if vals.get('start_date'):
            try:
                date_obj = fields.Date.from_string(vals.get('start_date'))
                date_str = date_obj.strftime('%y%m%d')
            except Exception:
                date_str = ''
        manager = self.env['hr.employee'].browse(vals.get('manager_id')) if vals.get('manager_id') else False
        base_code = manager.base_code if manager else ''
        product_obj = self.env['product.product'].browse(vals.get('product_id')) if vals.get('product_id') else False
        product_name = product_obj.name if product_obj else ''
        vals['name'] = f"{date_str}-{base_code}-{product_name}"
        return super().create(vals)
