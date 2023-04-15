# Generated by Django 4.2 on 2023-04-15 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название', max_length=50, verbose_name='Название компании')),
                ('location', models.CharField(help_text='Введите местоположения', max_length=50, verbose_name='Место нахождения')),
                ('email', models.EmailField(help_text='Введите почту', max_length=50, verbose_name='Почта')),
                ('phone', models.IntegerField(help_text='Введите название', verbose_name='Телефон')),
                ('date_create', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('date_update', models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления')),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название', max_length=50, verbose_name='ФИО')),
                ('role', models.CharField(blank=True, choices=[('LPR', 'ЛПР'), ('LVR', 'ЛВР'), ('MANAGER', 'Менеджер')], default='MANAGER', max_length=50, verbose_name='Должность')),
                ('email', models.EmailField(help_text='Введите почту', max_length=50, verbose_name='Почта')),
                ('phone', models.IntegerField(help_text='Введите название', verbose_name='Телефон')),
                ('date_create', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('date_update', models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companies', to='manager_base.company')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Введите название', max_length=50, verbose_name='Комментарий')),
                ('date_create', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('date_update', models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='manager_base.company')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ['-date_update'],
            },
        ),
    ]