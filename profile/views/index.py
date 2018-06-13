from django.shortcuts import render

from stauth.settings import DEBUG
from main.models import User
from main.views.auth import get_user


def info(request):
    user = get_user(request)
    if not isinstance(user, User):
        return user

    return render(request, 'profile_content/info.html', {'user': user, 'debug': DEBUG})


def instruction(request):
    user = get_user(request)
    if not isinstance(user, User):
        return user

    return render(request, 'profile_content/instruction.html', {'user': user, 'debug': DEBUG})
