from django.shortcuts import render, get_object_or_404
from company.models import Company


def view_company(request, slug):
    company = get_object_or_404(Company, slug=slug)
    founders = company.founders.all()
    # founders = Profile.obje
    return render(request,'company/company.html', {
        'company': company,
        'founders': founders
    })


def view_companys(request):
    companys = Company.objects.all()
    return render(request,'company/companys.html', {
        'companys': companys
    })
