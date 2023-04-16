from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView

from manager_base.models import Company


# Create your views here.


class CompanyCreateView(CreateView):
    model = Company
    template_name = 'manager_base/create_company.html'
    fields = ['name', 'location', 'email', 'phone']


class CompanyListView(ListView):
    model = Company
    template_name = 'manager_base/show_companies.html'


def home(request):
    return render(request, 'manager_base/base.html')