from django.shortcuts import HttpResponseRedirect, Http404, resolve_url
import urllib.parse as up


def login(request):
    if request.method == 'GET':
        # success = request.GET.get('success')
        url = 'https://confid.ru/openid-connect/auth'
        client_id = 'students'
        response_type = 'code'
        state = 'none'
        redir = up.quote('http://reg.mati.su/oidc_callback', safe='')
        # 'state={state}&scope=email%20openid%20profile&redirect_uri={redirect_uri}' \
        redirect_url = '{url}?response_type={response_type}&client_id={client_id}&' \
                       'state={state}&scope=email%20openid%20profile&redirect_uri={redir}' \
            .format(url=url,
                    response_type=response_type,
                    client_id=client_id,
                    state=state,
                    redir=redir)
        response = HttpResponseRedirect(redirect_url)
        return response
    else:
        raise Http404
