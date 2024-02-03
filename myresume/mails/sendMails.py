from django.core import mail
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect

from myresume.mails.email import EmailMyresume
from myresume.mails.emailForm import EmailMyresumeForm

DEFAULT_EMAIL_HOST = 'myresumemail00@gmail.com'
DEFAULT_RECEIVE_EMAIL = 'nghiaphamhong99@gmail.com'


def SendMail(request):
    if request.method == 'POST':
        connection = mail.get_connection()
        connection.open()
        email = EmailMyresume()
        form = EmailMyresumeForm(request.POST)
        email.your_name = form.data['your_name']
        email.your_email = form.data['your_email']
        email.email_subject = "Suggestion email"
        email.email_description = form.data['email_description']
        recipients = [DEFAULT_RECEIVE_EMAIL]

        email.save()
        send_mail(email.email_subject, email.email_description, DEFAULT_EMAIL_HOST, recipients)
        request.session['message'] = True
        return redirect("/")
    else:
        return redirect("/")
