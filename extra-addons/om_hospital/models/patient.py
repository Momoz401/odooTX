# -*- coding: utf-8 -*-
from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "医院病人"

    name = fields.Char(string='姓名', required=True)
    age = fields.Integer(string='年龄')
    gender = fields.Selection([
        ('male','男'),
        ('female','女'),
        ('other','其他'),
    ], string='性别', required=True, default='male')
    note = fields.Text(string='描述')