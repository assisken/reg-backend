from django.shortcuts import redirect, render
import main.utils as utils
from main.models import User
from .make_home import make_home


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

    return redirect('profile:index')


def get_user(request):
    try:
        user_id = request.session['user-id']
        user = User.objects.get(pk=user_id)
    except (KeyError, User.DoesNotExist):
        return redirect('main:login')

    if not user.email_verified:
        return render(request, 'email_verification.html')
    elif not user.linux_user:
        return make_home(request, user)

    return user
