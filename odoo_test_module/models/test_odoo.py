# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, tools, api

class test_odoo(models.Model):
    _name = "test.odoo"
    _description = "Test odoo"
    
    def _compute_total(self):
        for item in self:
            item.total = item.unit_price * item.count

    name = fields.Char(string="Name", required=True)
    unit_price = fields.Float(string="Unit price")
    count = fields.Float(string="Count")
    total = fields.Float(compute='_compute_total', string="Total")