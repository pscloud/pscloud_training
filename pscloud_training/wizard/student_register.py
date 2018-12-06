# -*- coding: utf-8 -*-

from odoo import api, fields, models

class StudentRegiester(models.TransientModel):
    _name = 'pscloud.training.student.regiester'
    _description = "学生注册"

    student_ids = fields.Many2many('res.partner', string='学生', domain=[('is_student', '=', True)])

    @api.multi
    def regiester(self):
        lesson_ids = self.env['pscloud.training.lesson'].browse(self._context.get('active_ids', []))
        for wizard in self:
            for lesson in lesson_ids:
                lesson.write({
                    'student_ids': [(4, id) for id in wizard.student_ids.ids]
                })
        return {'type': 'ir.actions.act_window_close'}


#  vim:et:si:sta:ts=4:sts=4:sw=4:tw=79:
