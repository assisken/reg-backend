from django.shortcuts import render
from django.http import Http404
from main.models import Student


def index(request):
    if request.method == 'GET':
        try:
            pk = request.session['user-id']
        except KeyError:
            stud = 'Не авторизован'
        else:
            stud = Student.objects.get(pk=pk)

        return render(request, 'index.html', {'info': stud})
    else:
        raise Http404
