# -*- coding: utf-8 -*-

from odoo import api, fields, models

class TrainingSubject(models.Model):
    _name = 'pscloud.training.subject'
    _description = "科目"

    name = fields.Char(string='名称')
    person_id = fields.Many2one('res.partner', string='负责人')
    lesson_ids = fields.One2many('pscloud.training.lesson', 'subject_id', string='课程')
    desc = fields.Text(string='描述')

#  vim:et:si:sta:ts=4:sts=4:sw=4:tw=79:
