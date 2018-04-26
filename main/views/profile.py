from django.shortcuts import redirect, render
from main.models import Student


def profile(request):
    try:
        id = request.session['user-id']
    except KeyError:
        return redirect('main:login')
    else:
        student = Student.objects.get(pk=id)

    return render(request, 'profile.html', {'student': student})
