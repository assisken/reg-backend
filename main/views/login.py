from django.shortcuts import HttpResponseRedirect, Http404
import urllib.parse as up


def login(request):
    if request.method == 'GET':
        url = 'https://confid.ru/openid-connect/auth'
        client_id = 'students'
        response_type = 'code'
        state = 'none'
        # redir = up.quote('http://reg.mati.su')
        # 'state={state}&scope=email%20openid%20profile&redirect_uri={redirect_uri}' \
        redirect_url = '{url}?response_type={response_type}&client_id={client_id}&' \
                       'state={state}&scope=email%20openid%20profile' \
            .format(url=url,
                    # redirect_uri=redir,
                    response_type=response_type,
                    client_id=client_id,
                    state=state)
        response = HttpResponseRedirect(redirect_url)
        return response
    else:
        raise Http404
