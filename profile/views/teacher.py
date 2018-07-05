from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

from main.models.teacher import Teacher
from main.models.user import User
from profile.mixins import UserRequired
from stauth.settings import DEBUG


class TeacherView(UserRequired, View):
    def get(self, request: HttpRequest, user: User):
        return render(request, 'profile_content/teacher.html', {
            'user': user,
            'debug': DEBUG,
            'teacher': Teacher.objects.get()
        })
