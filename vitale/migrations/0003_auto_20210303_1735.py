# Generated by Django 3.1.7 on 2021-03-03 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vitale', '0002_auto_20210303_1721'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='department_of_birth',
            new_name='department_of_Birth',
        ),
    ]