from . import db

class Property(db.Model):

    __tablename__ = 'property_profiles'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    bedrooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    property_type = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(10000))
    photo = db.Column(db.String(1000), nullable=False)

    def __init__(self, title, bedrooms, bathrooms, location, price, property_type, description, photo):
        #self.id = id
        self.title = title
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.location = location
        self.price = price
        self.property_type = property_type
        self.description = description
        self.photo = photo

    def __repr__(self):
        return '<Property %r>' % self.title