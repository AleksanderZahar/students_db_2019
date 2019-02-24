# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students_app', '0003_student_student_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exams',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exam_subject', models.CharField(max_length=256, verbose_name='\u041d\u0430\u0437\u0432\u0430 \u043f\u0440\u0435\u0434\u043c\u0435\u0442\u0443')),
                ('exam_date', models.DateTimeField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0456\u0441\u043f\u0438\u0442\u0443')),
                ('exam_teacher', models.CharField(max_length=256, verbose_name='\u0412\u0438\u043a\u043b\u0430\u0434\u0430\u0447')),
                ('exam_group', models.ForeignKey(verbose_name='\u0413\u0440\u0443\u043f\u0430', to='students_app.Group')),
            ],
            options={
                'verbose_name': '\u0406\u0441\u043f\u0438\u0442',
                'verbose_name_plural': '\u0406\u0441\u043f\u0438\u0442\u0438',
            },
            bases=(models.Model,),
        ),
    ]
