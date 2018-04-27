from django.shortcuts import render, redirect
from django.http import Http404

from main.models import User
from main.forms import LinuxUser


def index(request):
    if request.method == 'GET':
        try:
            pk = request.session['user-id']
            user = User.objects.get(pk=pk)
        except (KeyError, User.DoesNotExist):
            return render(request, 'index.html')

        if user.linux_user:
            return render(request, 'profile.html', {'user': user})
        else:
            return redirect('main:make_home')

    else:
        raise Http404
