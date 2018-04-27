from django.shortcuts import render, redirect
from django.http import Http404

from main.models import User


def index(request):
    if request.method == 'GET':
        try:
            pk = request.session['user-id']
            user = User.objects.get(pk=pk)
        except (KeyError, User.DoesNotExist):
            user = None
        else:
            return render(request, 'profile.html', {'user': user})

        return render(request, 'index.html', {'user': user})
    else:
        raise Http404
