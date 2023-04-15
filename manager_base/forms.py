from django import forms  # Импортируем модуль forms, из него возьмём класс ModelForm

from .models import Company, Contact, Comment  # Импортируем модель, чтобы связать с ней форму

class CompanyForm(forms.ModelForm):
    class Meta:
        # Эта форма будет работать с моделью Company
        model = Company

        # Здесь перечислим поля модели, которые должны отображаться в веб-форме;
        # при необходимости можно вывести в веб-форму только часть полей из модели.
        fields = ('name', 'location', 'email', 'phone')


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact

        # Здесь перечислим поля модели, которые должны отображаться в веб-форме;
        # при необходимости можно вывести в веб-форму только часть полей из модели.
        fields = ('name', 'role', 'email', 'phone', 'company')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment

        # Здесь перечислим поля модели, которые должны отображаться в веб-форме;
        # при необходимости можно вывести в веб-форму только часть полей из модели.
        fields = ('text', 'company', 'email', 'phone')