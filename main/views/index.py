from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from stauth.settings import DEBUG
from main.models import User


class Index(View):
    template_name = 'index.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        try:
            request.session['user-id']
        except (KeyError, User.DoesNotExist):
            return render(request, self.template_name, {'debug': DEBUG})
        return redirect('profile:instruction')
