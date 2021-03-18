from . import db

class UserProperty(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'user_property'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(180))
    number_of_bedrooms = db.Column(db.String(180))
    number_of_bathrooms = db.Column(db.String(180))
    location = db.Column(db.String(180))
    price = db.Column(db.String(180))
    types = db.Column(db.String(180))
    description = db.Column(db.String(180))
    filename= db.Column(db.String(300))

    def __init__(self,title,number_of_bedrooms,number_of_bathrooms,location,price,types,description,filename):
        self.title=title
        self.number_of_bedrooms=number_of_bedrooms
        self.number_of_bathrooms=number_of_bathrooms
        self.location=location
        self.price=price
        self.types=types
        self.description=description
        self.filename=filename

    def __repr__(self):
        return '<User %r>' % (self.username)