import urllib.parse as up
import requests
from django.shortcuts import render, resolve_url, HttpResponseRedirect


def auth(request):
    state = request.GET.get('state')
    if state != 'none':
        return render(request, 'index.html', {'info': 'Что-то пошло не так, повторите попытку...'})

    code = request.GET.get('code')
    client_id = 'students'
    client_secret = 'StarchausMudak'
    grant_type = 'authorization_code'
    redirect_uri = up.quote('https://client.example.org/cb', safe='')
    url = 'https://confid.ru/openid-connect/token'
    auth_header = 'Basic {client_id}:{client_secret}'.format(client_id=client_id, client_secret=client_secret)

    headers = {
        'Host': 'confid.ru',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': up.quote(auth_header, safe='')
    }
    data = (
        'grant_type={grant_type}&code={code}&redirect_uri={redirect_uri}&client_id={client_id}&'
        'client_secret={client_secret}') \
        .format(grant_type=grant_type,
                redirect_uri=redirect_uri,
                client_id=client_id,
                client_secret=client_secret,
                code=code)
    r = requests.post(url, headers=headers, data=data)
    token = r.json()['access_token']

    resp = HttpResponseRedirect(resolve_url('main:profile'))
    resp.set_cookie('token', token)
    return resp
