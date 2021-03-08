from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import datetime

GENDERS = [
    ("m", "male"),
    ("f", "female")
]

DEPARTMENTS = [
    ("01", "Auvergne-Rhône-Alpes"),
    ("02", "Hauts-de-France"),
    ("03", "Auvergne-Rhône-Alpes"),
    ("04", "Alpes-de-Haute-Provence"),
    ("05", "Provence-Alpes-Côte d'Azur"),
]

alphanumeric = RegexValidator(
    r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

numeric = RegexValidator(r'^[0-9+]', 'Only digit characters.')


def validate_date_of_birth(value):
    todays_date = datetime.today()
    if value > datetime.date(todays_date.replace(todays_date.year-16, todays_date.month, todays_date.day)):
        raise ValidationError(
            _('Vous devez avoir 16 ans ou plus')
        )

# add start end date validator


class User(models.Model):
    first_name = models.CharField(max_length=60, validators=[alphanumeric])
    last_name = models.CharField(max_length=60, validators=[alphanumeric])
    date_of_birth = models.DateField(validators=[validate_date_of_birth])
    gender = models.CharField(max_length=10, choices=GENDERS)
    department_of_birth = models.CharField(max_length=60, choices=DEPARTMENTS)
    social_security_number = models.CharField(
        max_length=60, validators=[numeric], unique=True)
    start_date = models.DateField(default=datetime.now)
    end_date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def clean(self, *args, **kwargs):
        social_security_number_is_valid = True
        gender = '0'
        if self.gender == 'm':
            gender = '1'
        if self.gender == 'f':
            gender = '2'

        # checking if the length of the socialSecurity number is valid
        if len(self.social_security_number) != 13:
            social_security_number_is_valid = False

        # checking if the gender is valid in the social security number
        if self.social_security_number[0] != gender:
            social_security_number_is_valid = False

        # checking if the birth year is valid in the social security number
        if self.social_security_number[1:3] != str(self.date_of_birth.year)[2:4]:
            social_security_number_is_valid = False

        # checking if the birth month is valid in the social security number
        if self.social_security_number[3:5] != str(self.date_of_birth.month).zfill(2):
            social_security_number_is_valid = False

        # checking if the department of birth is valid in the social security number
        if self.social_security_number[5:7] != self.department_of_birth:
            social_security_number_is_valid = False

        if not social_security_number_is_valid:
            raise ValidationError(
                _('Un ou plusieurs champs ne sont pas valides')
            )
        if self.start_date > self.end_date:
            raise ValidationError(
                _('La date de début doit être inférieure à la date de fin')
            )
