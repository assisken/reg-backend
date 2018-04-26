from .models import Student
import urllib.parse as up
import requests


def fetch_token(code):
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
    try:
        token = r.json()['access_token']
    except KeyError:
        token = r.json()
    return token


def fetch_user(token):
    url = 'https://confid.ru/openid-connect/userinfo'
    headers = {
        'Host': 'confid.ru',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Authorization: Bearer {token}'.format(token=token)
    }
    r = requests.post(url, headers=headers)
    return r.json()


def lazy_add_user(user):
    try:
        student = Student.objects.get(sub=int(user['sub']))
    except Student.DoesNotExist:
        student = Student.objects.create(
            name=user['name'],
            family_name=user['family_name'],
            given_name=user['given_name'],
            middle_name=user['middle_name'],
            nickname=user['nickname'],
            preferred_username=user['preferred_username'],
            profile=user['profile'],
            picture=user['picture'],
            website=user['website'],
            gender=user['gender'],
            birthdate=user['birthdate'],
            zoneinfo=user['zoneinfo'],
            # locale=user['locale'],
            updated_at=user['updated_at'],
            email=user['email'],
            email_verified=user['email_verified'],
            sub=user['sub']
        )
        student.save()
    return student
