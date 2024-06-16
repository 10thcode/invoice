"""
A flask application
"""
from flask import Flask, jsonify, url_for
from api.v1.routes import blueprint
from db import init_db
from flask_cors import CORS
from os import environ


app = Flask(__name__)
CORS(app)
init_db(app)
app.register_blueprint(blueprint, url_prefix="/api/v1/invoices")


@app.route("/", methods=["GET"])
def index():
    """
    Handle HTTP requests to / api endpoint
    """
    return jsonify({
        "invoices_url": url_for("blueprint.invoices"),
    }), 200


@app.route("/keys/domain", methods=["GET"])
def domain():
    """
    Get Auth0 tenant domain
    """
    return environ.get("AUTH0_DOMAIN"), 200


@app.route("/keys/client", methods=["GET"])
def client():
    """
    Get Auth0 client ID
    """
    return environ.get("AUTH0_CLIENT_ID"), 200


@app.route("/keys/audience", methods=["GET"])
def audience():
    """
    Get Auth0 API audience url
    """
    return environ.get("AUTH0_AUDIENCE"), 200


if __name__ == "__main__":
    app.run()
