from django.db import models
from django.db.models import ForeignKey
from django.urls import reverse


# Create your models here.
class Company(models.Model):
    name = models.CharField('Название компании', max_length=50, help_text="Введите название")
    location = models.CharField('Место нахождения', max_length=50, help_text="Введите местоположения")
    email = models.EmailField('Почта', max_length=50, help_text="Введите почту")
    phone = models.IntegerField('Телефон', help_text="Введите название")
    date_create = models.DateTimeField('Дата создания', auto_now=True)  # не нужно добавлять в форму
    date_update = models.DateTimeField('Дата обновления', auto_now_add=True)  # не нужно добавлять в форму

    class Meta:
        ordering = ["name"]
        verbose_name = "Компания"
        verbose_name_plural = "Компании"

    def __str__(self):
        return self.name

    def get_absolute_url(self):  # Тут мы создали новый метод
        return reverse('details-company', args=[str(self.id)])


class Contact(models.Model):
    ROLES = [('ЛПР', 'ЛПР'),
             ('ЛВР', 'ЛВР'),
             ('Менеджер', 'Менеджер')]
    name = models.CharField('ФИО', max_length=50, help_text="Введите название")
    role = models.CharField('Должность', max_length=50, choices=ROLES, default='Менеджер')
    email = models.EmailField('Почта', max_length=50, help_text="Введите почту")
    phone = models.IntegerField('Телефон', help_text="Введите название")
    date_create = models.DateTimeField('Дата создания', auto_now=True)  # не нужно добавлять в форму
    date_update = models.DateTimeField('Дата обновления', auto_now_add=True)  # не нужно добавлять в форму
    company = ForeignKey('Company', on_delete=models.CASCADE)

    class Meta:
        ordering = ["role"]
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return self.name


class Comment(models.Model):

    text = models.TextField('Комментарий', max_length=100, help_text="Введите название")
    date_create = models.DateTimeField('Дата создания', auto_now=True)  # не нужно добавлять в форму
    date_update = models.DateTimeField('Дата обновления', auto_now_add=True)  # не нужно добавлять в форму
    need_call = models.BooleanField('Поставить дату след звонка', null=True)
    date_next_call = models.DateTimeField('Дата след. звонка', null=True)
    company = ForeignKey('Company', on_delete=models.CASCADE)

    class Meta:
        ordering = ["date_update"]
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return self.text
