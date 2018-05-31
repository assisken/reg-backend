from django.shortcuts import redirect, render

from stauth.settings import DEBUG
from main.views.make_home import make_home
from main.models import User


def info(request):
    try:
        user_id = request.session['user-id']
        user = User.objects.get(pk=user_id)
    except (KeyError, User.DoesNotExist):
        return redirect('main:login')

    if not user.linux_user:
        return make_home(request, user)

    return render(request, 'profile_content/info.html', {'user': user, 'debug': DEBUG})


def instruction(request):
    try:
        user_id = request.session['user-id']
        user = User.objects.get(pk=user_id)
    except (KeyError, User.DoesNotExist):
        return redirect('main:login')

    if not user.linux_user:
        return make_home(request, user)

    return render(request, 'profile_content/instruction.html', {'user': user, 'debug': DEBUG})
