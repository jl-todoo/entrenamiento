# -*- coding: utf-8 -*-

 from odoo import models, fields


 class modelo2a(models.Model):
    _name = 'modelo2a.modelo2a'
     _description = 'modelo2a.modelo2a'

     Nombre = fields.Char()
     Valor = fields.Integer()
     Monto = fields.Float(compute="_value_pc", store=True)
     Descripcion = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
