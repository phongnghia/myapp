from django.contrib import admin

from myresume.models import Resume, Technical, DetailTechnical, OtherImage, Company, CompaniesWorked, Project


# Register your models here.

class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthday', 'position',)
    search_fields = ('name',)


class TechnicalAdmin(admin.ModelAdmin):
    list_display = ('tech_name',)
    search_fields = ('tech_name',)


class DetailTechnicalAdmin(admin.ModelAdmin):
    list_display = ('name', 'tech_name',)
    search_fields = ('name',)


class OtherImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name',)
    search_fields = ('company_name',)


class CompaniesWorkedAdmin(admin.ModelAdmin):
    list_display = ('name', 'company_name', 'company_exp',)
    search_fields = ('name', 'company_name',)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'project_name',)
    search_fields = ('name', 'project_name',)


admin.site.register(Resume, ResumeAdmin)
admin.site.register(Technical, TechnicalAdmin)
admin.site.register(DetailTechnical, DetailTechnicalAdmin)
admin.site.register(OtherImage, OtherImageAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(CompaniesWorked, CompaniesWorkedAdmin)
admin.site.register(Project, ProjectAdmin)
