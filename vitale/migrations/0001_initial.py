# Generated by Django 3.1.7 on 2021-03-03 15:40

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])),
                ('last_name', models.CharField(max_length=60, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('m', 'male'), ('f', 'female')], max_length=10)),
                ('department_of_Birth', models.CharField(choices=[('01', 'Auvergne-Rhône-Alpes'), ('02', 'Hauts-de-France'), ('03', 'Auvergne-Rhône-Alpes'), ('04', 'Alpes-de-Haute-Provence'), ('05', "Provence-Alpes-Côte d'Azur")], max_length=60)),
                ('social_security_number', models.CharField(max_length=60, unique=True, validators=[django.core.validators.RegexValidator('^[0-9+]', 'Only digit characters.')])),
                ('start_date', models.DateField(default=datetime.datetime.now)),
                ('end_date', models.DateField(default=datetime.datetime.now)),
            ],
        ),
    ]
