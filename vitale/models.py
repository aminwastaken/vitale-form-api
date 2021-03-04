from django.db import models
from  django.core.validators import RegexValidator
from datetime import datetime

GENDERS = [
    ("m", "male"),
    ("f","female")
]

DEPARTMENTS = [
    ("01","Auvergne-Rhône-Alpes"),
    ("02","Hauts-de-France"),
    ("03","Auvergne-Rhône-Alpes"),
    ("04","Alpes-de-Haute-Provence"),
    ("05","Provence-Alpes-Côte d'Azur"),
]

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
numeric = RegexValidator(r'^[0-9+]', 'Only digit characters.')

class User(models.Model):
    first_name = models.CharField(max_length=60,validators=[alphanumeric])
    last_name = models.CharField(max_length=60, validators=[alphanumeric])
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDERS)
    department_of_birth = models.CharField(max_length=60, choices=DEPARTMENTS)
    social_security_number = models.CharField(max_length=60,validators=[numeric],unique=True)
    start_date = models.DateField(default=datetime.now)
    end_date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.first_name + " " + self.last_name
