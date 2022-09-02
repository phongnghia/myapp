from django.contrib import admin

from myresume.models import My_resume, My_technical, Detail_technical

# Register your models here.

admin.site.register(My_resume)
admin.site.register(My_technical)
admin.site.register(Detail_technical)
