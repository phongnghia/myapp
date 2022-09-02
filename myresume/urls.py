from django.contrib import admin
from django.urls import path, include

import myresume.views

urlpatterns = [
    path('myresume/', myresume.views.List_Myresume, name='myresume')
]
