"""
Defines a class to validate auth0 jwt bearer token.
"""
import json
from urllib.request import urlopen
from authlib.oauth2.rfc7523 import JWTBearerTokenValidator
from authlib.jose.rfc7517.jwk import JsonWebKey


class Auth0JWTBearerTokenValidator(JWTBearerTokenValidator):
    """
    Validation class for auth0 jwt bearer token.
    """
    def __init__(self, domain, audience):
        """
        Initialize validation object.

        Args:
            domain: the auth0 tenant domain.
            audience: auth0 unique identifier for the api.
        """
        issuer = "https://{}/".format(domain)
        jsonurl = urlopen("{}.well-known/jwks.json".format(issuer))
        public_key = JsonWebKey.import_key_set(
            json.loads(jsonurl.read())
        )
        super(Auth0JWTBearerTokenValidator, self).__init__(
            public_key
        )
        self.claims_options = {
            "exp": {"essential": True},
            "aud": {"essential": True, "value": audience},
            "iss": {"essential": True, "value": issuer},
        }
