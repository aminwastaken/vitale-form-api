# Generated by Django 3.1.7 on 2021-03-04 10:32

from django.db import migrations, models
import vitale.models


class Migration(migrations.Migration):

    dependencies = [
        ('vitale', '0004_auto_20210303_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(validators=[vitale.models.validate_date_of_birth]),
        ),
    ]
