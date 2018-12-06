# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ResParter(models.Model):
    _inherit = 'res.partner'

    is_teacher = fields.Boolean(string='老师')
    is_student = fields.Boolean(string='学生')

#  vim:et:si:sta:ts=4:sts=4:sw=4:tw=79:
