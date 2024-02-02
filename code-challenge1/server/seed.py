from models import Restaurant,Restaurant_Pizza,Pizza, db
from random import choice as rc
from app import app


with app.app_context():
    # Clear existing hero data from the database
    Pizza.query.delete()
    Restaurant.query.delete()
    Restaurant_Pizza.query.delete()

    # Seed new restaurant data
    restaurants = [
        { 'name': "Wingmans", 'address': "Kirby Shoals, Lake Krista" },
        { 'name': "The garden", 'address': "Tyron Viaduct, East Carita" },
        { 'name': "Nacho palace", 'address': "Weissnat Squares, New Carroltown" },
        { 'name': "B pizzas", 'address': "Merlin Roads, Port Darrellport" },
        {'name': "The Winstonian", 'address': "Sanford Loop, Port Walter" }
    ]

    for restaurant in restaurants:
        new_Restaurant = Restaurant(**restaurant)
        db.session.add(new_Restaurant) 
        db.session.commit()

     # Seed new pizza data
    # pizzas = [
    #     { "name": "Kamala Khan", "super_name": "Ms. Marvel" },
    #     { "name": "Doreen Green", "super_name": "Squirrel Girl" },
    #     { "name": "Gwen Stacy", "super_name": "Spider-Gwen" },
    #     { "name": "Janet Van Dyne", "super_name": "The Wasp" },
    #     { "name": "Wanda Maximoff", "super_name": "Scarlet Witch" },
    #     { "name": "Carol Danvers", "super_name": "Captain Marvel" },
    #     { "name": "Jean Grey", "super_name": "Dark Phoenix" },
    #     { "name": "Ororo Munroe", "super_name": "Storm" },
    #     { "name": "Kitty Pryde", "super_name": "Shadowcat" },
    #     { "name": "Elektra Natchios", "super_name": "Elektra" }
    # ]

    # for hero in heroes:
    #     new_hero = Hero(**hero)
    #     db.session.add(new_hero)

    # # Commit changes to the database
    # db.session.commit()

    # # Seed data for Restaurant_Pizza

    restaurant_data = Restaurant.query.all()
    # pizza_data = Pizza.query.all()

    restaurant_pizza = []

        
    for restaurant_data in restaurant_data:
        data = Restaurant_Pizza(
        # 
        # price = rc(prices),
        # pizza_id = rc(pizza_data).id,
        restaurant_id = rc(restaurant_data).id
        )

    restaurant_pizza.append(data)
    db.session.add_all(restaurant_pizza)
    db.session.commit()

print( "🦸‍♀️ Done seeding!")