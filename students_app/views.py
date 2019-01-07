# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader

# Create your views here.

# def students_list(request, sid):
#     try:
#         sid=int(sid)
#     except ValueError:
#         raise Http404
#     else:
#         return HttpResponse('<h1>Hello World</h1>')

# def students_list(request):
#     return HttpResponse('<h1>Hello World</h1>')

# def students_list(request):
#     template = loader.get_template('demo.html')
#     context = RequestContext(request, {})
#     return HttpResponse(template.render(context))

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

# Views for Groups:


def groups_list(request):
    return HttpResponse('<h1>Groups Listing</h1>')


def groups_add(request):
    return HttpResponse('<h1>Groups Add Form</h1>')


def groups_edit(request, gid):
    return HttpResponse('<h1>Groups %s Edit Form</h1>' % gid)


def groups_delete(request, gid):
    return HttpResponse('<h1>Groups %s Delete</h1>' % gid)
