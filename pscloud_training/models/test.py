# -*- coding: utf-8 -*-

from . import lesson
from . import subject
from . import res_partner



lesson_obj = self.env.get('pscloud.training.lesson')
lesson_obj.create({
    'name': '英文写作',
    'start_date': '2018-10-01',
    'end_date': '2018-12-01',
    'seat_qty': 30,
})

lesson_obj.read(lesson_id, ['id', 'name', 'start_date'])

{
    'id': 2,
    'name': '英文写作',
    'start_date': '2018-10-01',
}


lesson_obj.browse(2).write({'start_date': '2018-10-01', 'end_date': '2018-12-01',})

lesson_obj.browse(2).write({'start_date': '2018-10-01', 'end_date': '2018-12-01',})

lesson_obj.browse(2).unlink()


lesson_obj.search([('seat_qty', '>', 10)])


lesson_obj.browse(2).copy()

for lesson in lesson_obj.browse([1,2,3]):
    pass



    @api.multi
    def name_get(self):
        return [(lesson.id, '%s:%s' % (lesson.name, lesson.teacher_id.name)) for lesson in self]




#  vim:et:si:sta:ts=4:sts=4:sw=4:tw=79:
