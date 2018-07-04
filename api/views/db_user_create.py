import json

from django.http import HttpResponse, HttpRequest
from django.views import View
from mysql import connector

from main.models import User
from profile.forms import DbPassResetForm
from profile.mixins import UserRequired
from stauth.settings import DB_CONFIG


class DbUserCreate(UserRequired, View):
    def post(self, request: HttpRequest, user: User) -> HttpResponse:
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
            return HttpResponse(json.dumps(resp, ensure_ascii=False))

        password = form.cleaned_data.get('db_password')
        host = DB_CONFIG.get('client', 'host')

        try:
            con = connector.connect(
                user=DB_CONFIG.get('client', 'user'),
                password=DB_CONFIG.get('client', 'password'),
                host=host,
            )
            cur = con.cursor()
            cur._defer_warnings = False
            cur.execute("CREATE USER IF NOT EXISTS %s@%s IDENTIFIED BY %s;",
                        (user.linux_user, host, password))
            cur.execute("GRANT ALL ON `{}_%`.* TO %s@%s;".format(user.linux_user),
                        (user.linux_user, host))
        except Exception as e:
            resp['type'] = 'danger'
            resp['message'] = str(e)
            return HttpResponse(json.dumps(resp, ensure_ascii=False))
        else:
            cur.close()
            con.close()

        user.db_password = password
        user.save()
        resp['type'] = 'success'
        resp['message'] = 'Пароль успешно установлен!'
        return HttpResponse(json.dumps(resp, ensure_ascii=False))