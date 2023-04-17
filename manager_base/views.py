from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView

from manager_base.forms import CompanyForm
from manager_base.models import Company


# Create your views here.


class CompanyCreateView(CreateView):
    model = Company
    template_name = 'manager_base/create_company.html'
    form_class = CompanyForm


class CompanyListView(ListView):
    model = Company
    template_name = 'manager_base/show_companies.html'
    context_object_name = 'companies'


class CompanyDetailsView(DetailView):
    model = Company
    template_name = 'manager_base/company_details.html'
    context_object_name = 'company'

