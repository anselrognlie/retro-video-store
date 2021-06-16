from flask import Blueprint, request, make_response, jsonify
from app.models.customer import Customer

bp = Blueprint("customers", __name__, url_prefix="/customers")

@bp.route("/", methods=("GET",), strict_slashes=False)
def get_customers():
    customers = [customer.to_json() for customer in Customer.query.all()]
    return make_response(jsonify(customers), 200)
