from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from manager_base.forms import CompanyForm, CommentForm
from manager_base.models import Company, Comment


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


class CompanyDeleteView(DeleteView):
    model = Company
    template_name = 'manager_base/delete_company.html'
    success_url = reverse_lazy("home")


class CompanyUpdateView(UpdateView):
    model = Company
    template_name = 'manager_base/create_company.html'
    success_url = reverse_lazy("home")
    form_class = CompanyForm


class CommentCreateView(CreateView):
    model = Comment
    template_name = 'manager_base/create_comment.html'
    success_url = reverse_lazy("home")
    form_class = CommentForm

    def form_valid(self, form):
        comp = Company.objects.get(id=self.kwargs['pk'])
        form.instance.company_id = comp.id
        return super(CommentCreateView, self).form_valid(form)