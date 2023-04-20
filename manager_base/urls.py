"""
URL configuration for mdash project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from manager_base import views


urlpatterns = [
    path('', views.CompanyListView.as_view(), name='home'),
    path('create_company/', views.CompanyCreateView.as_view(), name='create-company'),
    path('company_details/<int:pk>', views.CompanyDetailsView.as_view(), name='details-company'),
    path('company_details/<int:pk>/create_comment', views.CommentCreateView.as_view(), name='create-comment'),
    path('<int:pk>/delete_company', views.CompanyDeleteView.as_view(), name='company-delete'),
    path('<int:pk>/update_company', views.CompanyUpdateView.as_view(), name='company-update'),
    path('<int:pk>/create_contact', views.ContactCreateView.as_view(), name='contact-create')

]
