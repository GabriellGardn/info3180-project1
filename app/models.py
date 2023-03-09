from . import db

class Property(db.Model):

    __tablename__ = 'property_profiles'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    bedrooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(200))
    photo = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Property %r>' % self.title