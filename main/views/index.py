from django.shortcuts import render, redirect
from django.http import Http404

from main.models import Student


def index(request):
    if request.method == 'GET':
        try:
            pk = request.session['user-id']
            stud = Student.objects.get(pk=pk)
        except (KeyError, Student.DoesNotExist):
            stud = None
        else:
            return render(request, 'profile.html', {'student': stud})

        return render(request, 'index.html', {'student': stud})
    else:
        raise Http404
