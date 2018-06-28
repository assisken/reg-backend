from django.core.validators import RegexValidator
from django.db import models

from main.models import User


class Database(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[RegexValidator(
            regex='^[a-zA-Z_]+$',
            message='Название БД некорректно.'
        )])
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    pname = models.CharField(primary_key=True, null=False, max_length=22, blank=True)

    def save(self, *args, **kwargs):
        self.pname = '{}_{}'.format(self.owner.linux_user, self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
