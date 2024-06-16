"""
Defines utility functions
"""
import json
from os import environ
from urllib.request import urlopen
from authlib.jose.rfc7517.jwk import JsonWebKey
from authlib.jose import jwt


def get_user_id(token):
    """
    Get user id from auth0 access token.

    WARNING: This method should only be called after
    the access token has been verified.

    Args:
        token: the auth0 access token.

    Returns:
        user_id: the user id from the payload of auth0 access token.
    """
    domain = environ.get("AUTH0_DOMAIN")
    jsonurl = urlopen("https://{}/.well-known/jwks.json".format(domain))
    public_key = JsonWebKey.import_key_set(
        json.loads(jsonurl.read())
    )
    claims = jwt.decode(token, public_key)
    user_id = claims.get("sub")
    return user_id
