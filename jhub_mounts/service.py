# jhub-mounts/service.py
#
# written by: Oliver Cordes 2022-03-25
# changed by: Oliver Cordes 2022-03-25


import os
import secrets
from functools import wraps

from jupyterhub.services.auth import HubOAuth


from flask import Flask, session, request, redirect, make_response

from .config import Config



def authenticated(f):
    """Decorator for authenticating with the Hub via OAuth"""

    @wraps(f)
    def decorated(*args, **kwargs):
        token = session.get("token")

        if token:
            user = auth.user_for_token(token)
        else:
            user = None

        if user:
            return f(user, *args, **kwargs)
        else:
            # redirect to login url on failed auth
            state = auth.generate_state(next_url=request.path)
            response = make_response(
                redirect(auth.login_url + '&state=%s' % state))
            response.set_cookie(auth.state_cookie_name, state)
            return response

    return decorated

# setup flask


app = Flask(__name__)
app.config.from_object(Config)

#prefix = os.environ.get('JUPYTERHUB_SERVICE_PREFIX', '/')

auth = HubOAuth(api_token=app.config['API_TOKEN'], cache_max_age=60)

# encryption key for session cookies
app.secret_key = secrets.token_bytes(32)


