# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# 2025/3/2
from odoo import fields, models


class ResUsersSettings(models.Model):
    _inherit = 'res.users.settings'

    homemenu_config = fields.Json(string="Home Menu Configuration", readonly=True)
