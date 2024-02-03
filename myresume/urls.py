from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

import myresume.views
import myresume.routers.resume

urlpatterns = [
    path(r'', myresume.views.SingleResume, name='myresume'),
    path(r'mails/', include('myresume.mails.urls')),
    # Update later
    #path('/myresume', myresume.views.SingleResume, name='myresume'),
    # path('api/', include('myresume.routers.resume'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
