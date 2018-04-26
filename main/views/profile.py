from django.shortcuts import render


def profile(request):
    # TODO: make session
    prof = {
        'surname': '',
        'name': '',
        'midname': '',
        'email': '',
        'avatar': ''
    }

    return render(request, 'profile.html', {'profile': prof})
