import requests
from django.shortcuts import render


def profile(request):
    url = 'https://confid.ru/openid-connect/userinfo'
    token = request.COOKIES['token']
    headers = {
        'Host': 'confid.ru',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Authorization: Bearer {token}'.format(token=token)
    }
    r = requests.post(url, headers=headers)
    user = r.json()
    prof = {
        'surname': user['family_name'],
        'name': user['given_name'],
        'midname': user['middle_name'],
        'email': user['email'],
        'avatar': user['picture']
    }

    return render(request, 'profile.html', {'profile': prof})
