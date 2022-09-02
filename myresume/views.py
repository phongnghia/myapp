import pickle

from django.shortcuts import render

from myresume.models import My_resume, My_technical


# Create your views here.

def List_Myresume(request):
    tech = My_technical.objects.get(pk=1)
    return render(request, "base.html", {'tech': tech})
