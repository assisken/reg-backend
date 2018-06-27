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
        resp = {'type': None, 'message': None}

        if pwd == pwdcnf:
            resp['type'] = 'success'
            resp['message'] = 'Пароль успешно обновлён!'
            reset_passwd(user.linux_user, pwd)
        else:
            resp['type'] = 'danger'
            resp['message'] = 'Пароли не совпадают.'

        if not form.is_valid():
            resp['type'] = 'danger'
            resp['message'] = 'Форма невалидна. Что делать — ума не приложу.'
        return HttpResponse(json.dumps(resp, ensure_ascii=False))
