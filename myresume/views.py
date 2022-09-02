import pickle

from django.http import HttpResponse
from django.shortcuts import render

from myresume.models import My_resume, My_technical


# Create your views here.

def List_Myresume(request):
    return HttpResponse(My_resume.objects.get(pk=1))
