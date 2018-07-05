from django.db import models

from main.models.user import User


class StudGroup(models.Model):
    name = models.CharField(max_length=30, unique=True)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name
