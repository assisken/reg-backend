from django.shortcuts import redirect, render, Http404
from django.urls import reverse_lazy
from django.views import View

from main.forms import LinuxUser
from main.models import User
from main.utils.general import allowed_username, create_home, home_exists, username_exists
from stauth.settings import CREATE_HOME


class MakeHome(View):
    template_name = 'make_home.html'
    form_class = LinuxUser
    success_url = reverse_lazy('profile:instruction')

    def get(self, request, _):
        return render(request, 'make_home.html', {'form': self.form_class})

    def post(self, request, user):
        form = self.form_class(request.POST)
        linux_name = request.POST.get('linux_name', '')
        pwd = request.POST.get('pwd', '')
        pwdcnf = request.POST.get('pwdcnf', '')

        print(linux_name, pwd, pwdcnf)

        if pwd != pwdcnf:
            return self.error(request, 'Пароли не совпадают')
        elif not form.is_valid():
            return self.error(request,
                              'Вы ввели данные неправильно. Попробуйте ввести правильно!')
        elif home_exists(linux_name):
            return self.error(request,
                              'Такой пользователь уже существует')
        elif username_exists(linux_name):
            return self.error(request,
                              'Такой пользователь уже существует')
        elif not allowed_username(linux_name):
            return self.error(request,
                              'Такой пользователь уже существует')

        if CREATE_HOME:
            create_home(linux_name, pwd)
        user_filter = User.objects.filter(pk=user.id)
        user_filter.update(linux_user=linux_name)

        return redirect('profile:instruction')

    def error(self, request, error):
        return render(request, 'make_home.html', {'form': self.form_class, 'error': error})


def make_home(request, user):
    if user.linux_user:
        return redirect('profile:index')

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

    return redirect('profile:instruction')
