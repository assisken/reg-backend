from django.shortcuts import render
from django.views import View

from profile.forms import LinuxPassResetForm, DatabasePassForm
from profile.mixins import UserRequired
from stauth.settings import DEBUG, MAX_DB


class ProfileControlPanel(UserRequired, View):
    def get(self, request, user):
        return render(request, 'profile_content/control_panel.html', {
            'user': user,
            'debug': DEBUG,
            'pass_reset_form': LinuxPassResetForm(auto_id=False),
            'db_pass_form': DatabasePassForm(auto_id=False),
            'max_db': MAX_DB,
            'db_select': tuple('{}_{}'.format(user.linux_user, i+1) for i in range(user.db_count)),
        })
