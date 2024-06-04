"""
Initialize database
"""
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from os import environ


def init_db(app):
    """
    Initialize database

    Args:
        app: a flask application object
    """
    uri = environ.get("MONGO_URI")
    mongo_client = MongoClient(uri, server_api=ServerApi("1"))
    app.config["MONGO_CLIENT"] = mongo_client
    invoice_collection = app.config["MONGO_CLIENT"].invoice_db.invoices
    app.config["INVOICE_COLLECTION"] = invoice_collection
