from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)

    # relationship
    restaurant_pizza = db.relationship('Restaurant_Pizza', backref='restaurant')

    # serialize
    def serialize(self):
        return {  "id": self.id,"name": self.name,"address": self.address }  
       
         

class Pizza(db.Model,SerializerMixin):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)
    created_at = db.Column(db.Integer, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # relationship
    restaurant_pizza = db.relationship('Restaurant_Pizza', backref='pizza')
    # serialize
    def serialize(self):
        return {  "id": self.id,"name": self.name,"ingredients": self.ingredients, 'created_at':self.created_at }


class Restaurant_Pizza(db.Model,SerializerMixin):
    __tablename__ = 'restaurant_pizzas'

    id = db.Column(db.Integer, primary_key = True)
    # relationship
    pizza_id = db.Column(db.Integer, db.ForeignKey( 'pizzas.id'))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # validates price
    @validates('price')
    def validate_price(self, key, value):
        if (value > 30):
            raise ValueError('Price must be less than 30')
        return value
    
    # serialize
    def serialize(self):
        return {  "id": self.id,"price": self.price, "pizza_id":self.pizza_id }



 