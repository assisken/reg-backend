from stauth.settings import BASE_DIR
import urllib.parse as up
import subprocess as sp
import requests

from main.models import User


def fetch_token(code):
    client_id = 'students'
    client_secret = 'StarchausMudak'
    grant_type = 'authorization_code'
    redirect_uri = up.quote('http://reg.mati.su/oidc_callback', safe='')
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
        student = User.objects.get(sub=int(user['sub']))
    except User.DoesNotExist:
        student = User.objects.create(
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


def allowed_username(name):
    names = (
        'root', 'admin', 'adm', 'support', 'webmaster', 'db', 'database', 'mysql', 'server', 'www', 'php', 'http',
        'testing', 'test', 'config', 'options', 'example', 'name', 'us', 'mx', 'aa', 'af', 'ak', 'sq', 'am', 'ar',
        'an', 'hy', 'as', 'av', 'ae', 'ay', 'az', 'bm', 'ba', 'eu', 'be', 'bn', 'bh', 'bi', 'bs', 'br', 'bg', 'my',
        'ca', 'ch', 'ce', 'ny', 'zh', 'cv', 'kw', 'co', 'cr', 'hr', 'cs', 'da', 'dv', 'nl', 'dz', 'en', 'eo', 'et',
        'ee', 'fo', 'fj', 'fi', 'fr', 'ff', 'gl', 'ka', 'de', 'el', 'gn', 'gu', 'ht', 'ha', 'he', 'hz', 'hi', 'ho',
        'hu', 'ia', 'id', 'ie', 'ga', 'ig', 'ik', 'io', 'is', 'it', 'iu', 'ja', 'jv', 'kl', 'kn', 'kr', 'ks', 'kk',
        'km', 'ki', 'rw', 'ky', 'kv', 'kg', 'ko', 'ku', 'kj', 'la', 'lb', 'lg', 'li', 'ln', 'lo', 'lt', 'lu', 'lv',
        'gv', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mh', 'mn', 'na', 'nv', 'nd', 'ne', 'ng', 'nb', 'nn', 'no',
        'ii', 'nr', 'oc', 'oj', 'cu', 'om', 'or', 'os', 'pa', 'pi', 'fa', 'pl', 'ps', 'pt', 'qu', 'rm', 'rn', 'ro',
        'ru', 'sa', 'sc', 'sd', 'se', 'sm', 'sg', 'sr', 'gd', 'sn', 'si', 'sk', 'sl', 'so', 'st', 'es', 'su', 'sw',
        'ss', 'sv', 'ta', 'te', 'tg', 'th', 'ti', 'bo', 'tk', 'tl', 'tn', 'to', 'tr', 'ts', 'tt', 'tw', 'ty', 'ug',
        'uk', 'ur', 'uz', 've', 'vi', 'vo', 'wa', 'cy', 'wo', 'fy', 'xh', 'yi', 'yo', 'za', 'zu', 'reset', 'error',
        'home', 'index', 'login', 'auth', 'registration', 'logout', 'pass-remind', 'passremind', 'get', 'edit',
        'maiauth', 'acceptmail', 'profile', 'about', 'contact', 'contacts', 'tos', 'new', 'register', 'privacy',
        'products', 'apps', 'status', 'cgi-bin', 'cgi-xml', 'cgi', 'exe', 'passwd', 'htaccess', 'htpasswd', 'html',
        'htm', 'css', 'ns', 'ns1', 'ns2', 'ns3', 'ns4', 'ns5', 'ns6', 'ns7', 'ns8', 'ns9', 'ns10', 'openid', 'oauth',
        'oauth2', 'userinfo', 'openid-connect'
    )

    for n in names:
        if name == n:
            return False
    return True


def username_exists(name):
    try:
        User.objects.get(linux_user=name)
    except User.DoesNotExist:
        return False
    else:
        return True


def home_exists(name):
    res = sp.run('cut -d: -f1 /etc/passwd', stdout=sp.PIPE, shell=True)
    logins = res.stdout.decode('utf-8').split('\n')
    for login in logins:
        if name == login:
            return True
    return False


def create_home(name, passwd):
    it = sp.run('sudo {base}/scripts/add.sh {name} {pwd}'.format(base=BASE_DIR, name=name, pwd=passwd),
                shell=True, stdout=sp.PIPE)
    print(it)
