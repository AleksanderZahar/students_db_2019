# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from datetime import datetime
from ..models.students import Student
from ..models.groups import Group

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
    # if form was postetd?:
    if request.method == "POST":
        # was form add button clicked?:
        if request.POST.get('add_button') is not None:
            # errors collection:
            errors = {}

            # data for student object
            data = {'middle_name': request.POST.get('middle_name'),
                    'notes': request.POST.get('notes')}

            # validate user input:
            first_name = request.POST.get('first_name', '').strip()
            if not first_name:
                errors['first_name'] = u"Ім'я є обов'язковим"
            else:
                data['first_name'] = first_name

            last_name = request.POST.get('last_name', '').strip()
            if not last_name:
                errors['last_name'] = u"Прізвище є обов'язковим"
            else:
                data['last_name'] = last_name

            birthday = request.POST.get('birthday', '').strip()
            if not birthday:
                errors['birthday'] = u"Дата народження є обов'язковою"
            else:
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                except Exception:
                    errors['birthday'] = u'Введіть дату у коректному форматі "РРРР-ММ-ДД"'
                else:
                    data['birthday'] = birthday

            ticket = request.POST.get('ticket', '').strip()
            if not ticket:
                errors['ticket'] = u"Номер студ квитка є обов'язковим"
            else:
                data['ticket'] = ticket

            student_group = request.POST.get('student_group', '').strip()
            if not student_group:
                errors['student_group'] = u"Оберіть групу для студента"
            else:
                groups = Group.objects.filter(pk=student_group)
                if len(groups) != 1:
                    errors['student_group'] = u"Оберіть коректну групу для студента"
                else:
                    data['student_group'] = groups[0]

            # TODO: стр. 306 валидация поля фото. Точно ли формат изображения? Макс. размер 2 Мб
            photo = request.FILES.get('photo')
            if photo:
                data['photo'] = photo

            # save student
            if not errors:
                # create student object
                student = Student(**data)
                student.save()

                # # redirect user to students list page
                # return HttpResponseRedirect(
                #     u'%s?status_message=Студента %s %s успішно додано!' %
                #     (reverse('home'), student.last_name, student.first_name))

                # redirect user to students list page
                return HttpResponseRedirect(
                    reverse('home'),
                    messages.success(request,
                                     u'Студента %s %s успішно додано!'
                                     % (student.last_name, student.first_name)))

            else:
                # render form with errors and previous user input
                return render(request, 'students/students_add.html',
                              {'groups': Group.objects.all().order_by('title'),
                               'errors': errors})
        elif request.POST.get('cancel_button') is not None:
            # redirect to home page on cancel button
            # return HttpResponseRedirect(u'%s?status_message=Додавання студента скасовано!' % reverse('home'))
            return HttpResponseRedirect(reverse('home'), messages.warning(request, u'Додавання студента скасовано!'))

    else:
        # initial form render
        return render(request, 'students/students_add.html',
                      {'groups': Group.objects.all().order_by('title')})


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