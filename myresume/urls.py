from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

import myresume.views

urlpatterns = [
    path('myresume/', myresume.views.SingleResume, name='myresume')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
