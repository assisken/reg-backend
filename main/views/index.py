from django.shortcuts import render, redirect
from django.http import Http404

from stauth.settings import DEBUG
from main.models import User


def index(request):
    if request.method == 'GET':
        try:
            pk = request.session['user-id']
            user = User.objects.get(pk=pk)
        except (KeyError, User.DoesNotExist):
            return render(request, 'index.html', {'debug': DEBUG})

        return redirect('profile:instruction')

    else:
        raise Http404
