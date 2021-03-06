# -*- coding: utf-8 -*-

from django.shortcuts import render
from django import forms
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from studentsdb.settings import ADMIN_EMAIL
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.views.generic.edit import FormView

from django.core.urlresolvers import reverse_lazy


# Contact Admin Form


class ContactForm(forms.Form):

    def __init__(self, *args, **kwargs):

        # call original initializator
        super(ContactForm, self).__init__(*args, **kwargs)

        # this helper objects allows us to customize form
        self.helper = FormHelper()

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        # self.helper.form_action = reverse('contact_admin')

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        # form buttons
        self.helper.add_input(Submit('send_button', u'Надіслати'))

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


# Contact Admin form as ClassBasedView:
# TODO: реализовать польностью форму контакта через класс. Обработка ошибок, сообщения
class ContactView(FormView):
    template_name = 'contact_admin/contact-form.html'
    form_class = ContactForm
    # success_url = '/email-sent/'
    success_url = reverse_lazy('contact-form')

    def form_valid(self, form):
        """This method is called for valid data"""
        subject = 'Send from my Django StudentsApp ' + form.cleaned_data['subject']
        message = form.cleaned_data['message']
        from_email = form.cleaned_data['from_email']
        messages.success(self.request, u"Повідомлення успішно відправлено!!!!!!")

        send_mail(subject, message, from_email, [ADMIN_EMAIL])
        return super(ContactView, self).form_valid(form)
