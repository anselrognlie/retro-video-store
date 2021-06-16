from app import db

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    release_date = db.Column(db.DateTime(timezone=True))
    total_inventory = db.Column(db.Integer, nullable=False, server_default="0")

    rentals = db.relationship('Rental', backref="video", lazy=True)
