from django.shortcuts import HttpResponse, HttpResponseRedirect


def login(request):
    if request.method == 'GET':
        url = 'https://confid.ru/openid-connect/auth'
        client_id = 'students'
        response_type = 'code'
        state = 'none'

        redirect_url = '{url}?response_type={response_type}&client_id={client_id}&' \
                       'state={state}&scope=email%20openid%20profile' \
            .format(url=url,
                    response_type=response_type,
                    client_id=client_id,
                    state=state)
        response = HttpResponseRedirect(redirect_url)
        return response
    else:
        return HttpResponse('test...')
