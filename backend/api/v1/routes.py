"""
Handle HTTP requests for all api endpoints
"""
from auth import require_auth
from flask import Blueprint, request, jsonify, current_app
from bson.objectid import ObjectId
from bson.json_util import dumps
from datetime import datetime
from json import loads


blueprint = Blueprint('blueprint', __name__)


@blueprint.route("/<id>", methods=["GET", "PUT", "DELETE"])
@require_auth(None)
def invoice(id):
    """
    Handel HTTP requests for /<id> api endpoint

    Args
        id: The invoice id
    """
    invoice_collection = current_app.config["INVOICE_COLLECTION"]

    if request.method == "GET":
        invoice_document = invoice_collection.find_one({"_id": ObjectId(id)})
        if invoice_document:
            return jsonify(loads(dumps(invoice_document))), 200
        else:
            return jsonify({"error": "Invoice not found"}), 404

    if request.method == "PUT":
        data = request.get_json()
        data["modified_at"] = datetime.now().isoformat()
        result = invoice_collection.update_one(
                {"_id": ObjectId(id)},
                {"$set": data}
        )
        if result.matched_count:
            return jsonify({"status": "Success"}), 200
        else:
            return jsonify({"error": "Invoice not found"}), 404

    if request.method == "DELETE":
        result = invoice_collection.delete_one({"_id": ObjectId(id)})
        if result.deleted_count:
            return jsonify({"status": "Success"}), 200
        else:
            return jsonify({"error": "Invoice not found"}), 404


@blueprint.route("/", methods=["GET", "POST"])
@require_auth(None)
def invoices():
    """
    Handle HTTP requests for api/v1/invoices/ endpoint.
    """
    invoice_collection = current_app.config["INVOICE_COLLECTION"]

    if request.method == "GET":
        invoice_documents = invoice_collection.find()
        return jsonify(loads(dumps(invoice_documents))), 200

    if request.method == "POST":
        data = request.get_json()
        data["created_at"] = datetime.now().isoformat()
        data["modified_at"] = datetime.now().isoformat()
        result = invoice_collection.insert_one(data)
        return jsonify({"id": str(result.inserted_id)}), 201
