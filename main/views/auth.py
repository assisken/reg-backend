from django.shortcuts import render, resolve_url
from django.shortcuts import HttpResponse, HttpResponseRedirect
import main.utils as utils


def auth(request):
    state = request.GET.get('state')
    if state != 'none':
        return render(request, 'index.html', {'info': 'Что-то пошло не так, повторите попытку...'})

    code = request.GET.get('code')

    try:
        token = utils.fetch_token(code)
    except KeyError:
        return HttpResponse('wrong token')

    user = utils.fetch_user(token)
    stud = utils.lazy_add_user(user)

    request.session['user-id'] = stud.id
    return render(request, 'profile.html', {'student': stud})
