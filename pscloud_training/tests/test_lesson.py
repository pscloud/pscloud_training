# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError, ValidationError

class TestLesson(TransactionCase):

    def setUp(self):
        super(TestLesson, self).setUp()

    def test_lesson(self):
        """
        正常流程
        """
        lesson = self.env['pscloud.training.lesson'].create({
            'name': '英语协作',
            'teacher_id': self.env.ref('pscloud_training.demo_training_subject').id,
            'start_date': '2018-01-01',
            'end_date': '2018-07-01',
            'seat_qty': 30,
            'subject_id': self.env.ref('pscloud_training.demo_training_subject').id,
            'student_ids': [(4, self.env.ref('pscloud_training.demo_training_student_1').id)],
        })

        lesson.action_confirm()

    def test_lesson_fail(self):
        """
        异常流程
        """
        with self.assertRaises(ValidationError):
            lesson_fail = self.env['pscloud.training.lesson'].create({
                'name': '英语听力',
                'teacher_id': self.env.ref('pscloud_training.demo_training_subject').id,
                'start_date': '2018-12-01',
                'end_date': '2018-07-01',
                'seat_qty': 30,
                'subject_id': self.env.ref('pscloud_training.demo_training_subject').id,
                'student_ids': [(4, self.env.ref('pscloud_training.demo_training_student_1').id)],
            })


#  vim:et:si:sta:ts=4:sts=4:sw=4:tw=79:
