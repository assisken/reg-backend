from django.shortcuts import render
from django.views import View

from profile.forms import LinuxPassResetForm
from profile.mixins import UserRequired
from stauth.settings import DEBUG


class ProfileControlPanel(UserRequired, View):
    def get(self, request, user):
        return render(request, 'profile_content/control_panel.html', {
            'user': user,
            'debug': DEBUG,
            'linux_pass_reset_form': LinuxPassResetForm
        })
