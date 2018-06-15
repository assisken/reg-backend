from django.shortcuts import redirect, render

from main.models import User
from main.views.make_home import make_home


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
