import json

from django.http import HttpResponseServerError, HttpResponse
from django.views import View
from mysql import connector

from profile.mixins import UserRequired
from stauth.settings import DB_CONFIG, MAX_DB


class DatabaseCreate(UserRequired, View):
    def post(self, request, user):
        resp = {'type': None, 'message': None}
        max_db = MAX_DB
        pwd = request.POST.get('pwd', '')
        pwdcnf = request.POST.get('pwdcnf', '')

        if pwd != pwdcnf:
            resp['type'] = 'danger'
            resp['message'] = 'Пароли не совпадают!'
            return HttpResponse(json.dumps(resp, ensure_ascii=False))

        if user.db_count == MAX_DB:
            resp['type'] = 'danger'
            resp['message'] = 'Больше создавать баз данных нельзя!'
            return HttpResponse(json.dumps(resp, ensure_ascii=False))

        try:
            database_name = '{}_{}'.format(user.linux_user, user.db_count+1)
            host = DB_CONFIG.get('client', 'host')

            con = connector.connect(
                user=DB_CONFIG.get('client', 'user'),
                password=DB_CONFIG.get('client', 'password'),
                host=host,
            )
            cur = con.cursor()
            cur._defer_warnings = False
            cur.execute("CREATE DATABASE IF NOT EXISTS {};".format(database_name))
            cur.execute("CREATE USER IF NOT EXISTS %s@%s IDENTIFIED BY %s;",
                        (user.linux_user, host, pwd))
            cur.execute("grant all on `{}_%`.* to %s@%s;".format(user.linux_user),
                        (user.linux_user, host))

            user.db_count += 1
            if user.db_count > max_db:
                user.db_count = max_db
            user.db_pass = pwd
            con.close()
            user.save()

            resp['type'] = 'success'
            resp['message'] = 'База данных успешно создана!'

        except Exception as e:
            resp['type'] = 'danger'
            resp['message'] = e
            raise HttpResponseServerError
        return HttpResponse(json.dumps(resp, ensure_ascii=False))
