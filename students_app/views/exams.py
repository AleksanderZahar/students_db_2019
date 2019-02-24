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

