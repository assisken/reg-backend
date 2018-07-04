from django.http import HttpRequest
from django.shortcuts import HttpResponse
from django.views import View
import json

from main.models import User
from profile.forms import LinuxPassResetForm
from profile.mixins import UserRequired
from main.utils.general import reset_passwd


class LinuxPassReset(UserRequired, View):
    form_class = LinuxPassResetForm

    def post(self, request: HttpRequest, user: User) -> HttpResponse:
        form = self.form_class(request.POST)
        pwd = request.POST['pwd']
        pwdcnf = request.POST['pwdcnf']
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
