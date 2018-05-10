from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
import main.utils as utils


def auth(request):
    state = request.GET.get('state')
    if state != 'none':
        return redirect('main:login')

    code = request.GET.get('code')

    token = utils.fetch_token(code)

    if not isinstance(token, str):
        return redirect('main:login')

    usr = utils.fetch_user(token)
    user = utils.lazy_add_user(usr)

    request.session['user-id'] = user.id
    request.session.set_expiry(0)

    return redirect('main:profile')
