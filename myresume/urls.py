from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

import myresume.views
import myresume.routers.resume

urlpatterns = [
    path('', myresume.views.SingleResume, name='myresume'),
    # Update later
    #path('/myresume', myresume.views.SingleResume, name='myresume'),
    # path('api/', include('myresume.routers.resume'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
