from django.urls import path

import myresume.api.test as api

urlpatterns = [
    path('resume/<int:pk_id>', api.GetResume),
]
