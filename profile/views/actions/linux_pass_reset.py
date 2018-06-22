from django.shortcuts import HttpResponse
from django.views import View
import json

from profile.forms import LinuxPassResetForm
from profile.mixins import UserRequired
from main.utils.general import reset_passwd


class LinuxPassReset(UserRequired, View):
    form_class = LinuxPassResetForm

    def post(self, request, user):
        form = self.form_class(request.POST)
        pwd = request.POST.get('pwd', '')
        pwdcnf = request.POST.get('pwdcnf', '')
        resp = {'success': None}

        if pwd == pwdcnf:
            resp['success'] = True
            reset_passwd(user.linux_user, pwd)
        else:
            resp['success'] = False
            resp['message'] = 'Пароли не совпадают.'
        return HttpResponse(json.dumps(resp, ensure_ascii=False))
