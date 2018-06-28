from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from stauth.settings import MAX_DB


class User(models.Model):
    LOCALES = (
        ('ru-RU', 'Российская'),
        ('en-US', 'English'),
    )

    # Есть в коде
    email = models.CharField(max_length=30)
    email_verified = models.BooleanField(default=False)
    family_name = models.CharField(max_length=255, default=None)
    given_name = models.CharField(max_length=255, default=None)
    middle_name = models.CharField(max_length=255, default=None)
    picture = models.CharField(max_length=40, default=None, null=True, blank=True)
    birthdate = models.DateField()
    locale = models.CharField(max_length=5, choices=LOCALES)

    # Нет в коде, но есть в API
    name = models.CharField(max_length=255, null=True, blank=True)
    nickname = models.CharField(max_length=255, null=True, blank=True)
    preferred_username = models.CharField(max_length=255, null=True, blank=True)
    profile = models.CharField(max_length=255, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=255, null=True, blank=True)
    zoneinfo = models.CharField(max_length=255, null=True, blank=True)
    sub = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    # Кастомные поля
    linux_user = models.CharField(max_length=20, null=True, blank=True)
    db_password = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return '[{sub}] {name} {family} {middle} ({pref})' \
            .format(sub=self.sub,
                    name=self.given_name,
                    family=self.family_name,
                    middle=self.middle_name,
                    pref=self.preferred_username)

    def get_avatar(self):
        if self.picture:
            return self.picture
        else:
            return 'default.png'

    def get_profile(self):
        return {
            'ФИО': '{} {} {}'.format(self.family_name, self.given_name, self.middle_name),
            'Дата рождения': self.birthdate.strftime('%d.%m.%Y'),
            'E-mail': self.email,
            'Домен': '{name}.mati.su'.format(name=self.linux_user)
        }
