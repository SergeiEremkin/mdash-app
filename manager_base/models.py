from django.db import models
from django.db.models import ForeignKey
from django.urls import reverse


# Create your models here.
ROLES = [('user', 'Аутентифицированный пользователь'),
         ('moderator', 'Модератор'),
         ('admin', 'Администратор')]


class Company(models.Model):
    name = models.CharField('Название компании', max_length=50, help_text="Введите название")
    location = models.CharField('Место нахождения', max_length=50, help_text="Введите местоположения")
    email = models.EmailField('Почта', max_length=50, help_text="Введите почту")
    phone = models.IntegerField('Телефон', help_text="Введите название")
    date_create = models.DateTimeField('Дата создания', auto_now=True)  # не нужно добавлять в форму
    date_update = models.DateTimeField('Дата обновления', auto_now_add=True)  # не нужно добавлять в форму

    class Meta:
        ordering = ["-name"]
        verbose_name = "Компания"
        verbose_name_plural = "Компании"

    def __str__(self):
        return self.name


class Contact(models.Model):
    ROLES = [('LPR', 'ЛПР'),
             ('LVR', 'ЛВР'),
             ('MANAGER', 'Менеджер')]
    name = models.CharField('ФИО', max_length=50, help_text="Введите название")
    role = models.CharField('Должность', max_length=50,blank=True, choices=ROLES, default='MANAGER')
    email = models.EmailField('Почта', max_length=50, help_text="Введите почту")
    phone = models.IntegerField('Телефон', help_text="Введите название")
    date_create = models.DateTimeField('Дата создания', auto_now=True)      # не нужно добавлять в форму
    date_update = models.DateTimeField('Дата обновления', auto_now_add=True)  # не нужно добавлять в форму
    company = ForeignKey('Company', on_delete=models.CASCADE, related_name='companies')

    class Meta:
        ordering = ["-name"]
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField('Комментарий', max_length=50, help_text="Введите название")
    date_create = models.DateTimeField('Дата создания', auto_now=True)      # не нужно добавлять в форму
    date_update = models.DateTimeField('Дата обновления', auto_now_add=True)  # не нужно добавлять в форму
    company = ForeignKey('Company', on_delete=models.CASCADE, related_name='comments')

    class Meta:
        ordering = ["-date_update"]
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return self.name
