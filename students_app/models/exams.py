# -*- coding: utf-8 -*-

from django.db import models


class Exams(models.Model):
    """Exams Model"""

    class Meta(object):
        verbose_name = u"Іспит"
        verbose_name_plural = u"Іспити"

    exam_subject = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Назва предмету")

    exam_date = models.DateTimeField(
        blank=False,
        verbose_name=u"Дата іспиту",
        null=True)

    exam_teacher = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Викладач")

    exam_group = models.ForeignKey(
        'Group',
        verbose_name=u'Група',
        blank=False,
        null=False)

    def __unicode__(self):
        return u"%s - %s (%s)" % (self.exam_subject, self.exam_group.title, self.exam_date.date())
