from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
import main.utils as utils


def auth(request):
    state = request.GET.get('state')
    if state != 'none':
        return render(request, 'index.html', {'info': 'Что-то пошло не так, повторите попытку...'})

    code = request.GET.get('code')

    token = utils.fetch_token(code)

    if not isinstance(token, str):
        return HttpResponse(str(token))

    usr = utils.fetch_user(token)
    user = utils.lazy_add_user(usr)

    request.session['user-id'] = user.id
    request.session.set_expiry(0)

    if user.linux_user:
        return redirect('main:profile')
    else:
        return redirect('main:make_home')

