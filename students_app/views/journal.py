# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, Http404

# Views for Journal:


def journal_list(request):
    visiting = (
        {'stud_id': 1,
         'stud_first_name': u'Віталій',
         'stud_last_name': u'Подоба'},
        {'stud_id': 2,
         'stud_first_name': u'Андрій',
         'stud_last_name': u'Корост'},
        {'stud_id': 3,
         'stud_first_name': u'Тарас',
         'stud_last_name': u'Бульба'},
        {'stud_id': 4,
         'stud_first_name': u'Олександр',
         'stud_last_name': u'Захаров'},
    )
    return render(request, 'students/journal_page.html', {'visiting': visiting})


def journal_student(request, jsid):
    return HttpResponse('<h1>Student %s Journal page</h1>' % jsid)


def journal_group(request, jgid):
    return HttpResponse('<h1>Group %s Journal page</h1>' % jgid)
