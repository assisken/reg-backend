from django.shortcuts import redirect
from django.views import View
from mysql import connector

from profile.mixins import UserRequired
from stauth.settings import DB_CONFIG


class DatabaseRemove(UserRequired, View):
    def post(self, request, user):
        try:
            database_name = '{}_{}'.format(user.linux_user, user.db_count)
            host = DB_CONFIG.get('client', 'host')
            con = connector.connect(
                user=DB_CONFIG.get('client', 'user'),
                password=DB_CONFIG.get('client', 'password'),
                host=host,
                raise_on_warnings=True
            )
            cur = con.cursor()
            cur.execute("DROP DATABASE IF EXISTS {}".format(database_name))
            user.db_count -= 1
            if user.db_count < 0:
                user.db_count = 0
            user.save()
            if user.db_count == 0:
                cur.execute("DROP USER IF EXISTS %s@%s",
                            (user.linux_user, host))
                user.db_pass = None
                user.save()
        except Exception as e:
            raise e
        return redirect('profile:panel')
