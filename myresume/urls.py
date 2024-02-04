from django.conf import settings
from django.urls import path, include, re_path
from django.views.static import serve

import myresume.views
import myresume.routers.resume

urlpatterns = [
    path(r'', myresume.views.SingleResume, name='myresume'),
    path(r'mails/', include('myresume.mails.urls')),
]

urlpatterns += [
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
]
