from django.shortcuts import redirect, render

from main.models import User
from stauth.settings import DEBUG
from main.utils.get_user import get_user


def control_panel(request):
    user = get_user(request)
    if not isinstance(user, User):
        return user

    return render(request, 'profile_content/control_panel.html', {'user': user, 'debug': DEBUG})
