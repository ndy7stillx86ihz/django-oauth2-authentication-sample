import secrets
import requests as req
import urllib3

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from oauthlib.oauth2 import WebApplicationClient
from authentication.utils import generate_pkce_pair

# Disable SSL warnings (only for development)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

CLIENT_ID = settings.OAUTH_CLIENT_ID

def login_view(request):
    authorization_url = settings.OAUTH_AUTHORIZATION_URI

    client = WebApplicationClient(CLIENT_ID)

    code_verifier, code_challenge = generate_pkce_pair()

    request.session['state'] = secrets.token_urlsafe(16) # csrf
    request.session['code_verifier'] = code_verifier

    url = client.prepare_request_uri(
        authorization_url,
        redirect_uri=settings.OAUTH_CALLBACK_URL,
        scope=settings.OAUTH_SCOPES,
        state=request.session['state'],
        code_challenge=code_challenge,
        code_challenge_method='S256',
        ui_locales="es_ES"
    )

    return redirect(url)


def callback_view(request):
    data = request.GET
    code = data['code']
    state = data.get('state', '')

    if request.session.get('state') != state or not code:
        messages.add_message(
            request,
            messages.ERROR,
            "State information mismatch!"
        )
        return redirect(reverse_lazy('authentication:login'))
    else:
        del request.session['state']


    client = WebApplicationClient(CLIENT_ID)

    response = req.post(
        settings.OAUTH_TOKEN_URI,
        headers={
            "content-type": "application/x-www-form-urlencoded"
        },
        data=client.prepare_request_body(
            code=code,
            redirect_uri=settings.OAUTH_CALLBACK_URL,
            client_id=CLIENT_ID,
            code_verifier=request.session['code_verifier']
        ),
        verify=settings.OAUTH_VERIFY_SSL
    )

    client.parse_request_body_response(response.text)

    response = req.get(settings.OAUTH_USERINFO_URI, headers={
        'Authorization': f'Bearer {client.token["access_token"]}'
    }, verify=settings.OAUTH_VERIFY_SSL)

    print("USERINFO RESPONSE:", response.text)
    print("TOKEN:", client.token)

    json_dict = response.json()

    request.session['profile'] = json_dict

    user, _ = User.objects.get_or_create(username=json_dict['username'])
    login(request, user)

    return redirect(reverse_lazy('demo:home'))


def logout_view(request):
    # fixme: no desautentica bien
    logout(request)
    params = {
        "client_id": CLIENT_ID,
        "post_logout_redirect_uri": request.build_absolute_uri(reverse_lazy("demo:home")),
        "state": request.session.get('state', '')
    }

    return redirect(params["post_logout_redirect_uri"])
