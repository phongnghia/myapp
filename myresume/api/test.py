from django.http import HttpResponse

from myresume.models import Resume


def GetResume(request, pk_id):
    resume = Resume.objects.filter(id=pk_id).get()
    return HttpResponse({'resume': resume})
