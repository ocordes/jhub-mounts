# jhub_mounts/routes.py

# written by: Oliver Cordes 2022-03-25
# changed by: Oliver Cordes 2022-03-25


from .service import app, auth, authenticated

import json
from flask import Response, request


@app.route(app.config['SERVICE_PREFIX'])
@authenticated
def whoami(user):
    return Response(
        json.dumps(user, indent=1, sort_keys=True), mimetype='application/json'
    )





@app.route(app.config['SERVICE_PREFIX'] + 'oauth_callback')
def oauth_callback():
    code = request.args.get('code', None)
    if code is None:
        return 403

    # validate state field
    arg_state = request.args.get('state', None)
    cookie_state = request.cookies.get(auth.state_cookie_name)
    if arg_state is None or arg_state != cookie_state:
        # state doesn't match
        return 403

    token = auth.token_for_code(code)
    # store token in session cookie
    session["token"] = token
    next_url = auth.get_next_url(cookie_state) or prefix
    response = make_response(redirect(next_url))
    return response
