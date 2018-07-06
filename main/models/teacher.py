from django.db import models

import json

from .stud_group import StudGroup
from .user import User


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    groups = models.ManyToManyField(StudGroup)

    def __str__(self):
        return '{} {} {}'.format(self.user.family_name, self.user.given_name, self.user.middle_name)
