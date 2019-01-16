# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader

# Views for Groups:


def groups_list(request):
    groups = (
        {'id': 1,
         'name': u'МтМ-21',
         'lead': u'Ячменев Олег'},
        {'id': 2,
         'name': u'МтМ-22',
         'lead': u'Подоба Віталій'},
        {'id': 3,
         'name': u'МтМ-23',
         'lead': u'Іванов Андрій'},
        {'id': 4,
         'name': u'МтМ-24',
         'lead': u'Васильов Сергій'},
    )
    return render(request, 'students/groups_list.html', {'groups': groups})


def groups_add(request):
    return HttpResponse('<h1>Groups Add Form</h1>')


def groups_edit(request, gid):
    return HttpResponse('<h1>Groups %s Edit Form</h1>' % gid)


def groups_delete(request, gid):
    return HttpResponse('<h1>Groups %s Delete</h1>' % gid)
