from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from manager_base.forms import CompanyForm, CommentForm, ContactForm
from manager_base.models import Company, Comment, Contact


# Create your views here.


class CompanyCreateView(CreateView):
    model = Company
    template_name = 'manager_base/create_company.html'
    form_class = CompanyForm

    def get(self, request, *args, **kwargs):
        context = {'form': CompanyForm(), 'title': 'Создание компании'}
        return render(request, 'manager_base/create_company.html', context)


class CompanyListView(ListView):
    model = Company
    template_name = 'manager_base/show_companies.html'
    context_object_name = 'companies'

    def get(self, request, *args, **kwargs):
        context = {'companies': Company.objects.all(), 'title': 'Список компаний'}
        return render(request, 'manager_base/show_companies.html', context)


class CompanyDetailsView(DetailView):
    model = Company
    template_name = 'manager_base/company_details.html'
    context_object_name = 'company'

    def get(self, request, *args, **kwargs):
        context = {'company': Company.objects.get(id=self.kwargs['pk']), 'title': 'Карточка компании'}
        return render(request, 'manager_base/company_details.html', context)


class CompanyDeleteView(DeleteView):
    model = Company
    template_name = 'manager_base/delete_company.html'
    success_url = reverse_lazy("home")
    context_object_name = 'company'
    def get(self, request, *args, **kwargs):
        company = Company.objects.get(id=self.kwargs['pk'])
        context = {'company': company,
                   'title': 'Удаление компании', 'company': company.name}
        return render(request, 'manager_base/delete_company.html', context)


class CompanyUpdateView(UpdateView):
    model = Company
    template_name = 'manager_base/create_company.html'
    success_url = reverse_lazy("home")
    form_class = CompanyForm
    context_object_name = 'company'

    def get(self, request, *args, **kwargs):
        company = Company.objects.get(id=self.kwargs['pk'])
        context = {'company': company, 'form': CompanyForm(instance=company),
                   'title': 'Редактирование компании'}
        return render(request, 'manager_base/create_company.html', context)


class CommentCreateView(CreateView):
    model = Comment
    template_name = 'manager_base/create_comment.html'
    success_url = reverse_lazy("home")
    form_class = CommentForm

    def get(self, request, *args, **kwargs):
        context = {'form': CommentForm(), 'title': 'Создание комментария'}
        return render(request, 'manager_base/create_comment.html', context)

    def form_valid(self, form):
        comp = Company.objects.get(id=self.kwargs['pk'])
        form.instance.company_id = comp.id
        return super(CommentCreateView, self).form_valid(form)


class ContactCreateView(CreateView):
    model = Contact
    template_name = 'manager_base/create_contact.html'
    success_url = reverse_lazy("home")
    form_class = ContactForm

    def get(self, request, *args, **kwargs):
        context = {'form': ContactForm(), 'title': 'Создание контакта'}
        return render(request, 'manager_base/create_comment.html', context)

    def form_valid(self, form):
        comp = Company.objects.get(id=self.kwargs['pk'])
        form.instance.company_id = comp.id
        return super(ContactCreateView, self).form_valid(form)
