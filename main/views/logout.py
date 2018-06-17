from django.shortcuts import redirect
from django.views import View


class Logout(View):
    @staticmethod
    def get(request):
        request.session.clear()
        return redirect('main:index')
