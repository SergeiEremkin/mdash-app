from django import forms  # Импортируем модуль forms, из него возьмём класс ModelForm

from .models import Company, Contact, Comment  # Импортируем модель, чтобы связать с ней форму


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'location', 'email', 'phone']

    name = forms.CharField(label='Компания', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите текст'}))
    location = forms.CharField(label='Местоположение', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите текст'}))
    email = forms.EmailField(label='Эл.почта', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите текст'}))
    phone = forms.IntegerField(label='Номер телефона', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'x(xxx)xxxxxxx'}))


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
        fields = ['text']
