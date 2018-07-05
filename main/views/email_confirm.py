import json

from django.http import HttpResponse, HttpResponseServerError, HttpRequest
from django.shortcuts import render, redirect
from django.views import View

from main.models.user import User
from main.utils.general import fetch_user
from stauth.settings import DEBUG


class EmailConfirm(View):
    def get(self, request: HttpRequest, user: User) -> HttpResponse:
        if user.email_verified:
            return redirect('profile:instruction')

        token = None
        try:
            token = request.session['token']
        except KeyError:
            request.session.clear()
            redirect('main:login')

        new_user = fetch_user(token)

        try:
            if new_user['error'] == 'invalid_token':
                request.session.clear()
                return redirect('main:login')
            else:
                if DEBUG:
                    return HttpResponse(json.dumps(new_user, ensure_ascii=False))
                else:
                    raise HttpResponseServerError
        except KeyError:
            pass

        if new_user['email_verified']:
            user.email_verified = True
            user.save()
            return redirect('profile:instruction')

        return render(request, 'email_confirm.html', {
            'user': user,
            'debug': DEBUG
        })
