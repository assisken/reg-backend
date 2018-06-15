from django.shortcuts import render
from django.views.generic import DetailView, ListView

from stauth.settings import DEBUG
from main.models import User
from main.utils.get_user import get_user


class ProfileIndex(DetailView):
    model = User
    template_name = 'profile_content/control_panel.html'
    pk_url_kwarg = 'user_id'

    def get_context_data(self, **kwargs):
        context = super(ProfileIndex, self).get_context_data(**kwargs)
        return context


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
