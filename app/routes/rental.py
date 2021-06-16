from flask import Blueprint, jsonify, request
from datetime import datetime, timedelta
from app import db
from app.models.rental import Rental

bp = Blueprint("rentals", __name__, url_prefix="/rentals")

@bp.route("/check-out", methods=("POST",), strict_slashes=False)
def create():
    request_body = request.get_json()

    # should validate params!

    # should validate whether there is inventory available!
    # can we determine the current available inventory
    # _without_ adding a specific column holding the _current_
    # inventory
    # hint: how can we get the number of existing rentals for this video?
    # recall from the flask shell example:
    # c = Customer.query.get(1)
    # c.rentals[0].video.rentals[0].customer.name  # look at all the helpers that are here!
    # What if we start with a video?

    rental = Rental(
        customer_id=request_body["customer_id"],
        video_id=request_body["video_id"],
        due_date=datetime.now() + timedelta(days=7)
    )

    db.session.add(rental)
    db.session.commit()

    return jsonify(dict(
        customer_id=rental.customer_id,
        video_id=rental.video_id,
        due_date=rental.due_date
    ))

