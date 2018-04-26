from django.shortcuts import render, HttpResponse


def make_home(request):
    return HttpResponse('test')
