from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

from main.models import User
from profile.mixins import UserRequired
from stauth.settings import DEBUG


class ProfileInfo(UserRequired, View):
    template_name = 'profile_content/info.html'

    def get(self, request: HttpRequest, user: User) -> HttpResponse:
        return render(request, self.template_name, {'user': user, 'debug': DEBUG})


class ProfileInstruction(UserRequired, View):
    template_name = 'profile_content/instruction.html'

    def get(self, request: HttpRequest, user: User) -> HttpResponse:
        return render(request, self.template_name, {'user': user, 'debug': DEBUG})
