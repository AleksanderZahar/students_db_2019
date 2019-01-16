# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Views for Students:


def students_list(request):
    students = (
        {'id': 1,
         'first_name': u'Віталій',
         'last_name': u'Подоба',
         'ticket': 2121,
         'image': 'img/me.jpeg'},
        {'id': 2,
         'first_name': u'Андрій',
         'last_name': u'Корост',
         'ticket': 2122,
         'image': 'img/piv.png'},
        {'id': 3,
         'first_name': u'Тарас',
         'last_name': u'Бульба',
         'ticket': 2123,
         'image': 'img/podoba3.jpg'},
        {'id': 4,
         'first_name': u'Олександр',
         'last_name': u'Захаров',
         'ticket': 2124,
         'image': 'img/podoba3.jpg'},
    )
    return render(request, 'students/students_list.html', {'students': students})


def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')


def students_edit(request, sid):
    return HttpResponse('<h1>Student %s Edit Form</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Student %s Delete</h1>' % sid)