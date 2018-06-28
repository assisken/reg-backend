from django.shortcuts import render
from django.views import View

from profile.forms import LinuxPassResetForm, DatabaseForm, DbPassResetForm, DbSelectMultipleForm
from profile.mixins import UserRequired
from profile.models import Database
from stauth.settings import DEBUG, MAX_DB


class ProfileControlPanel(UserRequired, View):
    def get(self, request, user):
        databases = Database.objects.filter(owner=user)
        return render(request, 'profile_content/control_panel.html', {
            'user': user,
            'debug': DEBUG,
            'pass_reset_form': LinuxPassResetForm(auto_id=False),
            'db_reset_pass_form': DbPassResetForm(auto_id=False),
            'db_form': DatabaseForm(auto_id=False),
            'db_multiple_form': DbSelectMultipleForm(user=user),
            'databases': databases
        })
