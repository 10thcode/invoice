"""
A flask application
"""
from flask import Flask, jsonify, url_for
from api.v1.routes import blueprint
from db import init_db
from flask_cors import CORS


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

if __name__ == "__main__":
    app.run()
