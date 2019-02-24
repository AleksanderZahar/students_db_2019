from django.conf.urls import patterns, include, url
from django.contrib import admin
from .settings import MEDIA_ROOT, DEBUG

urlpatterns = patterns('',
                       # Students urls:
                       url(r'^$', 'students_app.views.students.students_list', name='home'),
                       url(r'^students/add/$', 'students_app.views.students.students_add', name='students_add'),
                       url(r'^students/(?P<sid>\d+)/edit/$', 'students_app.views.students.students_edit',
                           name='students_edit'),
                       url(r'^students/(?P<sid>\d+)/delete/$', 'students_app.views.students.students_delete',
                           name='students_delete'),

                       # Groups urls:
                       url(r'^groups/$', 'students_app.views.groups.groups_list', name='groups'),
                       url(r'^groups/add/$', 'students_app.views.groups.groups_add', name='groups_add'),
                       url(r'^groups/(?P<gid>\d+)/edit/$', 'students_app.views.groups.groups_edit',
                           name='groups_edit'),
                       url(r'^groups/(?P<gid>\d+)/delete/$', 'students_app.views.groups.groups_delete',
                           name='groups_delete'),

                       # Journal urls:
                       url(r'^journal/$', 'students_app.views.journal.journal_list', name='journal'),
                       url(r'^journal/groups/(?P<jgid>\d+)/$', 'students_app.views.journal.journal_group',
                           name='group_journal'),
                       url(r'^journal/students/(?P<jsid>\d+)/$', 'students_app.views.journal.journal_student',
                           name='student_journal'),

                       # Exams list:
                       url(r'^exams/$', 'students_app.views.exams.exams_list', name='exams'),

                       url(r'^admin/', include(admin.site.urls)),
                       )
if DEBUG:
    # serve files from media folder
    urlpatterns += patterns('',
                            url(r'^media/(?P<path>.*)$',
                                'django.views.static.serve',
                                {'document_root': MEDIA_ROOT}))
