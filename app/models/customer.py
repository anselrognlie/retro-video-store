from app import db


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    postal_code = db.Column(db.Integer, nullable=False)
    phone_number = db.Column(db.String, nullable=False)
    registered_at = db.Column(db.DateTime(timezone=True), nullable=False,
                              server_default=db.func.now())

    rentals = db.relationship('Rental', backref="customer", lazy=True)

    def to_json(self):
        # return {
        #     "name": self.name,
        #     "postal_code": self.postal_code,
        #     # ...
        # }
        return dict(
            id=self.id,
            name=self.name,
            postal_code=self.postal_code,
            phone_number=self.phone_number,
            registered_at=self.registered_at,
        )        