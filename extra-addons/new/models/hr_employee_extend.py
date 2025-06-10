from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'   # 继承Odoo原生员工表

    base_code = fields.Char('基地代号')
