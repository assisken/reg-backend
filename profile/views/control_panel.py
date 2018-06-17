from django.shortcuts import render
from django.views import View

from profile.mixins import CheckUser
from stauth.settings import DEBUG


class ProfileControlPanel(CheckUser, View):
    def get(self, request, user):
        return render(request, 'profile_content/control_panel.html', {'user': user, 'debug': DEBUG})
