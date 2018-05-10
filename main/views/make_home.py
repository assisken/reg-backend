from django.shortcuts import redirect, render, HttpResponse, Http404
from stauth.settings import CREATE_HOME

from main.utils import allowed_username, create_home, home_exists, username_exists
from main.models import User
from main.forms import LinuxUser


def make_home(request, user):
    if user.linux_user:
        return redirect('main:profile')

    if request.method == 'GET':
        form = LinuxUser()
        return render(request, 'make_home.html', {'form': form})

    elif request.method == 'POST':
        form = LinuxUser(request.POST)
        linux_name = request.POST.get('linux_name', '')
        pwd = request.POST.get('pwd', '')
        pwdcnf = request.POST.get('pwdcnf', '')

        if pwd != pwdcnf:
            error = 'Пароли не совпадают'
        elif not form.is_valid():
            error = 'Вы ввели данные неправильно. Попробуйте ввести правильно!'
        elif home_exists(linux_name):
            error = 'Такой пользователь уже существует'
        elif username_exists(linux_name):
            error = 'Такой пользователь уже существует'
        elif not allowed_username(linux_name):
            error = 'Такой пользователь уже существует'
        else:
            error = None

    else:
        raise Http404

    if error:
        return render(request, 'make_home.html', {'form': form, 'error': error})

    if CREATE_HOME:
        create_home(linux_name, pwd)

    user_filter = User.objects.filter(pk=user.id)
    user_filter.update(linux_user=linux_name)

    return render(request, 'profile.html', {'user': user, 'success': 'Ваша учётная запись успешно создана.'})
