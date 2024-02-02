#!/usr/bin/env python3

from flask import Flask, make_response, request,make_response,jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Restaurant,Pizza,Restaurant_Pizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)

@app.route('/')
def home():
    return 'WELCOME TO PIZZA PALACE'

class Restaurants(Resource):
    def get(self):
        resrtand_dict = [restrand.serialize()for restrand in Restaurant.query.all()]
        response = make_response(jsonify(resrtand_dict),200)
        return response
    
api.add_resource(Restaurants, '/restaurants')

class RestaurantsById(Resource):
    def get(self,id):
        res_id = Restaurant.query.get(id)
        if not res_id:
            return {"error": "Restaurant not found"}
        else:
            res_dict = res_id.serialize()
            response = make_response(jsonify(res_dict), 200)
            return response
        
    def delete(self,id):
        res_id = Restaurant.query.get(id)
        if not res_id:
            return {"error": "Restaurant not found"}
        else:
            db.session.delete(res_id)
            db.session.commit()

            response = make_response(jsonify('Success: id deleted'))
            return response
        
api.add_resource(RestaurantsById, '/restaurants/<int:id>')

class Pizzas (Resource):
    def get(self): 
        pizza_dict = [pizza.serialize() for pizza in Pizza.query.all()]
        response = make_response(jsonify(pizza_dict), 200)
        return response
api.add_resource(Pizzas, '/pizzas')


class Restaurant_Pizzas(Resource):
    def post(self):
        data = request.get_json()
        price = data.get("price")
        pizza_id = data.get("pizza_id")
        restaurant_id = data.get("restaurant_id")

        new_data = Restaurant_Pizza(price = price, pizza_id = pizza_id,restaurant_id = restaurant_id)
        if not new_data:
            return{"errors": ["validation errors"]},404
        else:
            db.session.add(new_data)
            db.session.commit()

            data_dict = new_data.serialize()
            response = make_response(jsonify(data_dict),201)
            return response


api.add_resource(Restaurant_Pizzas, '/restaurant_pizzas')


if __name__ == '__main__':
    app.run(port=5555, debug=True)
