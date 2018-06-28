import json

from django.http import HttpResponse
from django.views import View
from mysql import connector

from profile.models import Database
from stauth.settings import DB_CONFIG


class DatabaseRemove(View):
    def post(self, request):
        resp = {'type': None, 'message': None}
        pname = request.POST.get('select', '')

        try:
            host = DB_CONFIG.get('client', 'host')
            con = connector.connect(
                user=DB_CONFIG.get('client', 'user'),
                password=DB_CONFIG.get('client', 'password'),
                host=host,
            )
            cur = con.cursor()
            cur._defer_warnings = False
            cur.execute("DROP DATABASE {};".format(pname))
        except Exception as e:
            resp['type'] = 'danger'
            resp['message'] = str(e)
            return HttpResponse(json.dumps(resp, ensure_ascii=False))
        else:
            cur.close()
            con.close()

        db = Database.objects.get(pname=pname)
        db.delete()

        resp['type'] = 'success'
        resp['message'] = 'База данных успешно удалена!'

        return HttpResponse(json.dumps(resp, ensure_ascii=False))
        # return redirect('profile:panel')
