import json

from django.db import IntegrityError
from django.http import HttpResponse, HttpRequest
from django.views import View
from mysql import connector

from main.models.user import User
from profile.forms import DatabaseForm
from profile.models import Database
from profile.mixins import UserRequired
from stauth.settings import DB_CONFIG, MAX_DB


class DatabaseCreate(UserRequired, View):
    def post(self, request: HttpRequest, user: User) -> HttpResponse:
        resp = {'type': None, 'message': None}

        form = DatabaseForm(request.POST)
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

        db_name = form.cleaned_data.get('name')

        databases = Database.objects.filter(owner=user)
        db_count = len(databases)

        if db_count >= MAX_DB:
            resp['type'] = 'danger'
            resp['message'] = 'Вы не божете создать больше, чем {}!'.format(MAX_DB)
            return HttpResponse(json.dumps(resp, ensure_ascii=False))

        try:
            host = DB_CONFIG.get('client', 'host')
            con = connector.connect(
                user=DB_CONFIG.get('client', 'user'),
                password=DB_CONFIG.get('client', 'password'),
                host=host,
            )
            cur = con.cursor()
            cur._defer_warnings = False
            cur.execute("CREATE DATABASE IF NOT EXISTS {}_{};".format(user.linux_user, db_name))
        except Exception as e:
            resp['type'] = 'danger'
            resp['message'] = str(e)
            return HttpResponse(json.dumps(resp, ensure_ascii=False))
        else:
            cur.close()
            con.close()

        try:
            db = Database.objects.create(name=db_name, owner=user)
            db.save()
        except IntegrityError:
            resp['type'] = 'danger'
            resp['message'] = 'База данных с таким именем уже существует!'
            return HttpResponse(json.dumps(resp, ensure_ascii=False))

        resp['type'] = 'success'
        resp['message'] = 'База данных успешно создана!'

        return HttpResponse(json.dumps(resp, ensure_ascii=False))
