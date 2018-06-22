from django.shortcuts import render
from django.views import View

from profile.mixins import UserRequired
from stauth.settings import DEBUG


class ProfileInfo(UserRequired, View):
    template_name = 'profile_content/info.html'

    def get(self, request, user):
        return render(request, self.template_name, {'user': user, 'debug': DEBUG})


class ProfileInstruction(UserRequired, View):
    template_name = 'profile_content/instruction.html'

    def get(self, request, user):
        return render(request, self.template_name, {'user': user, 'debug': DEBUG})
