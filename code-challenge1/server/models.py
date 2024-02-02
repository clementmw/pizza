from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)

    # relationship
    restaurant_pizza = db.relationship('Restaurant_Pizza', backref='restaurant')

    # serialize

class Pizza(db.Model):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)
    created_at = db.Column(db.Integer, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # relationship
    restaurant_pizza = db.relationship('Restaurant_Pizza', backref='pizza')


class Restaurant_Pizza(db.Model):
    __tablename__ = 'restaurant_pizzas'

    id = db.Column(db.Integer, primary_key = True)
    # relationship
    pizza_id = db.Column(db.Integer, db.ForeignKey( 'pizzas.id'))
    restrant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    price = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    # serialize



 