"""
Provides a decorator to protect private api endpoint.

require_auth: a decorator to protect private api endpoints
that need authentication before access.
"""
from os import environ
from flask import Flask, jsonify
from authlib.integrations.flask_oauth2 import ResourceProtector
from validator import Auth0JWTBearerTokenValidator


require_auth = ResourceProtector()

domain = environ.get("AUTH0_DOMAIN")
audience = environ.get("AUTH0_AUDIENCE")
validator = Auth0JWTBearerTokenValidator(domain, audience)

require_auth.register_token_validator(validator)
