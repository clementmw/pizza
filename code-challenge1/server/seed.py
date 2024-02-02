from models import Restaurant,Restaurant_Pizza,Pizza, db
from random import choice as rc
from app import app
from faker import Faker

fake = Faker()


with app.app_context():
    # Clear existing hero data from the database
    Pizza.query.delete()
    Restaurant.query.delete()
    Restaurant_Pizza.query.delete()

    # Seed new restaurant data
    restaurants = [
        { 'name': "Sottocasa NYC", 'address': "298 Atlantic Ave, Brooklyn, NY 11201" },
        { 'name': "PizzArte" ,'address': "69 W 55th St, New York, NY 10019" },
        { 'name': "Nacho palace", 'address': "Weissnat Squares, New Carroltown" },
        { 'name': "B pizzas", 'address': "Merlin Roads, Port Darrellport" },
        {'name': "The Winstonian", 'address': "Sanford Loop, Port Walter" }
    ]

    for restaurant in restaurants:
        new_Restaurant = Restaurant(**restaurant)
        db.session.add(new_Restaurant) 
        db.session.commit()

     # Seed new pizza data
    pizzas = [
        { 'name': "Cheese-pizza", 'ingredients': "Dough, Tomato Sauce, Cheese" },
        { 'name': "Pepperoni-pizza", 'ingredients':  "Dough, Tomato Sauce, Cheese, Pepperoni"},
        { 'name': "Hawaiian-pizza", 'ingredients': "Hawaiian" },
        { 'name': "Meat-pizza", 'ingredients': "Meat" },
        { 'name': "Veggie-pizza", 'ingredients': "Veggie"}
    ]

    for pizza in pizzas:
        new_pizza = Pizza(**pizza) 
        db.session.add(new_pizza)
    db.session.commit()

    # Seed data for Restaurant_Pizza
    restaurant_data = Restaurant.query.all()
    pizza_data = Pizza.query.all()

    restaurant_pizza = []

    for _ in range(10):  # Adjust the number as needed
        data = Restaurant_Pizza(
            price=fake.random_int(min=1, max=30),  
            pizza_id=rc(pizza_data).id,
            restaurant_id = rc(restaurant_data).id
        )
        restaurant_pizza.append(data)

    db.session.add_all(restaurant_pizza)
    db.session.commit()

print( "🦸‍♀️ Done seeding!")