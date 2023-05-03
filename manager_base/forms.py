from django import forms  # Импортируем модуль forms, из него возьмём класс ModelForm
from .models import Company, Contact, Comment  # Импортируем модель, чтобы связать с ней форму


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'location', 'email', 'phone']

    name = forms.CharField(label='Компания', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите текст', 'style': 'width: 500px'}))
    location = forms.CharField(label='Местоположение', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите текст', 'style': 'width: 500px'}))
    email = forms.EmailField(label='Эл.почта', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите текст', 'style': 'width: 500px'}))
    phone = forms.IntegerField(label='Номер телефона', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'x(xxx)xxxxxxx', 'style': 'width: 500px'}))


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact

        # Здесь перечислим поля модели, которые должны отображаться в веб-форме;
        # при необходимости можно вывести в веб-форму только часть полей из модели.
        fields = ['name', 'role', 'email', 'phone']

    name = forms.CharField(label='ФИО', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите текст', 'style': 'width: 500px'}))
    role = forms.ChoiceField(choices=Contact.ROLES, label='Должность', widget=forms.Select(
        attrs={'class': 'form-control', 'placeholder': 'Введите текст', 'style': 'width: 500px'}))
    email = forms.EmailField(label='Эл.почта', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите текст', 'style': 'width: 500px'}))
    phone = forms.IntegerField(label='Номер телефона', widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'x(xxx)xxxxxxx', 'style': 'width: 500px'}))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'need_call', 'date_next_call']

    text = forms.CharField(label='Комментарий', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите текст', 'style': 'width: 500px'}))
    need_call = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    date_next_call = forms.DateTimeField(required=False, widget=forms.SelectDateWidget())


