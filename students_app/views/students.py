# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..models.students import Student

# Views for Students:


def students_list(request):
    students = Student.objects.all()

    # try to order students list
    order_by = request.GET.get('order_by', '')
    if order_by in ('last_name', 'first_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()
    elif order_by in 'id':
        students = students.order_by('last_name')
        if request.GET.get('reverse', '') == '1':
            students = students.order_by('last_name').reverse()
    else:
        students = students.order_by('last_name')

    # paginate students
    paginator = Paginator(students, 3)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        students = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results
        students = paginator.page(paginator.num_pages)

    return render(request, 'students/students_list.html', {'students': students})


def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')


def students_edit(request, sid):
    return HttpResponse('<h1>Student %s Edit Form</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Student %s Delete</h1>' % sid)


# def students_list(request):
#     students = (
#         {'id': 1,
#          'first_name': u'Віталій',
#          'last_name': u'Подоба',
#          'ticket': 2121,
#          'image': 'img/me.jpeg'},
#         {'id': 2,
#          'first_name': u'Андрій',
#          'last_name': u'Корост',
#          'ticket': 2122,
#          'image': 'img/piv.png'},
#         {'id': 3,
#          'first_name': u'Тарас',
#          'last_name': u'Бульба',
#          'ticket': 2123,
#          'image': 'img/podoba3.jpg'},
#         {'id': 4,
#          'first_name': u'Олександр',
#          'last_name': u'Захаров',
#          'ticket': 2124,
#          'image': 'img/podoba3.jpg'},
#     )
#     return render(request, 'students/students_list.html', {'students': students})