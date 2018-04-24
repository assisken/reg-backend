from django.shortcuts import render
from django.http import Http404


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        raise Http404


