import pickle

from django.http import HttpResponse
from django.shortcuts import render

from myresume.models import Resume, Technical, DetailTechnical, CompaniesWorked, Company, OtherImage, Project
from myresume.mails.emailForm import EmailMyresumeForm, EditForm


# Create your views here.

def GetCompaniesWorked(name_id):
    list_company = CompaniesWorked.objects.filter(name_id=name_id)
    return list_company


def GetTechnical(tech_name_id):
    technical = Technical.objects.filter(id=tech_name_id).get()
    return technical


def GetCompanyInfor(company_name_id):
    return Company.objects.filter(id=company_name_id).get()


def GetOtherImage(name_id):
    return OtherImage.objects.filter(name_id=name_id)


def GetProject(name_id):
    return Project.objects.filter(name_id=name_id)


def GetDefaultMyresume():
    single_resume = Resume.objects.filter(id=1).get()
    list_detailTechnical = DetailTechnical.objects.filter(name_id=1)
    # get experience
    single_exp = single_resume.work_exp
    # get companies user
    list_companies_worked = GetCompaniesWorked(1)
    # list technical

    list_technical = []

    for detail in list_detailTechnical:
        technical = GetTechnical(detail.tech_name_id)
        list_technical.append(technical)

    # get companies information
    list_company = []
    for detail_i in list_companies_worked:
        company = GetCompanyInfor(detail_i.company_name_id)
        list_company.append(company)

    other_image = GetOtherImage(single_resume.id)

    list_project = GetProject(single_resume.id)

    form = EditForm()
    rendered_form = form.render("form_email.html")

    context = {
        'single_resume': single_resume,
        'list_detailTechnical': list_detailTechnical,
        'single_exp': single_exp,
        'list_company': list_company,
        'list_technical': list_technical,
        'hero_img': other_image[0].image,
        'intro_img': other_image[1].image,
        'list_project': list_project,
        'form': rendered_form
    }

    return context


def SingleResume(request):
    context = GetDefaultMyresume()
    return render(request, 'index.html', context)
