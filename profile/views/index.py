from django.shortcuts import render
from django.views import View

from profile.mixins import CheckUser
from stauth.settings import DEBUG


class ProfileInfo(CheckUser, View):
    template_name = 'profile_content/info.html'

    def get(self, request, user):
        return render(request, self.template_name, {'user': user, 'debug': DEBUG})


class ProfileInstruction(CheckUser, View):
    template_name = 'profile_content/instruction.html'

    def get(self, request, user):
        return render(request, self.template_name, {'user': user, 'debug': DEBUG})
