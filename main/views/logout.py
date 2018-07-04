from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect
from django.views import View


class Logout(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        request.session.clear()
        return redirect('main:index')
