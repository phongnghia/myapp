from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

import myresume.mails.sendMails

urlpatterns = [
    path(r'send_mail', myresume.mails.sendMails.SendMail, name='sendmail'),
]
