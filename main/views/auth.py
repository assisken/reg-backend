from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.views import View

import utils.general as utils


class Auth(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        state = request.GET.get('state', '')
        if state != 'none':
            return redirect('main:login')

        code = request.GET.get('code', '')
        token = utils.fetch_token(code)

        if not isinstance(token, str):
            return redirect('main:login')

        usr = utils.fetch_user(token)
        user = utils.lazy_add_user(usr)

        request.session['user-id'] = user.id
        request.session['token'] = token
        request.session.set_expiry(0)
        
        return redirect('profile:index')
