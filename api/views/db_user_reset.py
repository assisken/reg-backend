import json

from django.http import HttpResponse, HttpRequest
from django.views import View
from mysql import connector

from main.models.user import User
from profile.forms import DbPassResetForm
from profile.mixins import UserRequired
from stauth.settings import CONFIG


class DbUserReset(UserRequired, View):
    def post(self, request: HttpRequest, user: User):
        resp = {'type': None, 'message': None}
        form = DbPassResetForm(request.POST)

        if not form.is_valid():
            message = ''

            # TODO: обвязать функцией эту дрисню
            for _, error in form.errors.as_data().items():
                for vld_error in error:
                    for msg in vld_error:
                        message += msg

            resp['type'] = 'danger'
            resp['message'] = message
            return HttpResponse(json.dumps(resp, ensure_ascii=False), content_type='application/json')

        password = form.cleaned_data.get('db_password')
        host = CONFIG.get('database', 'host')

        try:
            con = connector.connect(
                user=CONFIG.get('database', 'user'),
                password=CONFIG.get('database', 'password'),
                host=host,
            )
            cur = con.cursor()
            cur._defer_warnings = False
            cur.execute("SET PASSWORD FOR %s@%s = PASSWORD(%s);",
                        (user.linux_user, host, password))
        except Exception as e:
            resp['type'] = 'danger'
            resp['message'] = str(e)
            return HttpResponse(json.dumps(resp, ensure_ascii=False), content_type='application/json')
        else:
            cur.close()
            con.close()

        user.db_password = password
        user.save()
        resp['type'] = 'success'
        resp['message'] = 'Новый пароль успешно установлен!'
        return HttpResponse(json.dumps(resp, ensure_ascii=False), content_type='application/json')
