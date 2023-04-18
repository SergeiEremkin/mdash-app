from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Company, Comment, Contact

admin.site.register(Company)
admin.site.register(Comment)
admin.site.register(Contact)