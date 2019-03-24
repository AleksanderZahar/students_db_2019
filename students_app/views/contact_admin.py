# -*- coding: utf-8 -*-

from django.shortcuts import render
from django import forms
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from studentsdb.settings import ADMIN_EMAIL, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD

# Contact Admin Form


class ContactForm(forms.Form):
    from_email = forms.EmailField(
        label=u"Ваша Емейл Адреса")
    subject = forms.CharField(
        label=u"Заголовок листа",
        max_length=128)
    message = forms.CharField(
        label=u"Текст повідомлення",
        widget=forms.Textarea)


def contact_admin(request):
    # check is form was posted
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)

        # check whether user data is valid:
        if form.is_valid():
            # send mail
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']

            try:
                send_mail(subject, message, from_email, [ADMIN_EMAIL])
            except Exception:
                # message = u"Під час відправки листа виникла непередбачувана помилка. Спробуйте пізніше"
                status_message = messages.error(request, u"Під час відправки листа виникла непередбачувана помилка."
                                                         u" Спробуйте пізніше")
            else:
                # message = u"Повідомлення успішно відправлено!"
                status_message = messages.success(request, u"Повідомлення успішно відправлено!")
            # redirect to same contact page with success message
            # return HttpResponseRedirect(
            #     u'%s?status_message=%s' % (reverse('contact_admin'), message))
            return HttpResponseRedirect(reverse('contact_admin'), status_message)
    # if there was not POST render blank form
    else:
        form = ContactForm()

    return render(request, 'contact_admin/form.html', {'form': form})
