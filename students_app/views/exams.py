# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..models.exams import Exams

# Views for Exams:


def exams_list(request):
    exam_list = Exams.objects.all()

    return render(request, 'students/exams_list.html', {'exam_list': exam_list})


def exam_add(request):
    return HttpResponse('<h1>Exam Add Form</h1>')


def exam_results(request, exid):
    return HttpResponse('<h1>Exam %s Results Table</h1>' % exid)


def exam_edit(request, exid):
    return HttpResponse('<h1>Exam %s Edit Form</h1>' % exid)


def exam_delete(request, exid):
    return HttpResponse('<h1>Exam %s Delete</h1>' % exid)
