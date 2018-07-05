from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View

from main.forms import LinuxUser
from main.models.user import User
from main.utils.general import allowed_username, create_home, home_exists, username_exists


class MakeHome(View):
    template_name = 'make_home.html'
    form_class = LinuxUser
    success_url = reverse_lazy('profile:instruction')

    def get(self, request: HttpRequest, _) -> HttpResponse:
        return render(request, 'make_home.html', {'form': self.form_class})

    def post(self, request: HttpRequest, user: User) -> HttpResponse:
        form = self.form_class(request.POST)
        linux_name = request.POST['linux_name']
        pwd = request.POST['pwd']
        pwdcnf = request.POST['pwdcnf']

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

        create_home(linux_name, pwd)
        user_filter = User.objects.filter(pk=user.id)
        user_filter.update(linux_user=linux_name)

        return redirect('profile:instruction')

    def error(self, request, error):
        return render(request, 'make_home.html', {'form': self.form_class, 'error': error})
