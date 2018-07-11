import json

from django.http import HttpResponse, HttpRequest
from django.views import View
from mysql import connector

from profile.models import Database
from stauth.settings import CONFIG


class DatabaseRemove(View):
    def post(self, request: HttpRequest) -> HttpResponse:
        resp = {'type': None, 'message': None}
        pname = request.POST['select']

        try:
            host = CONFIG.get('database', 'host')
            con = connector.connect(
                user=CONFIG.get('database', 'user'),
                password=CONFIG.get('database', 'password'),
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

        return HttpResponse(json.dumps(resp, ensure_ascii=False), content_type='application/json')
        # return redirect('profile:panel')
