from odoo import models, fields

class NewModel(models.Model):
    _name = 'new.model'
    _description = 'New Model'

    name = fields.Char('名称')
