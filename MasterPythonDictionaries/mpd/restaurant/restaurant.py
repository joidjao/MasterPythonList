restaurants = [
    {"name": "The Gourmet Kitchen", "cuisine_type": "Italian"},
    {"name": "Sushi Palace", "cuisine_type": "Japanese"},
    {"name": "Burger World", "cuisine_type": "American"},
    {"name": "Spice Route", "cuisine_type": "Indian"},
    {"name": "Le Petite Bistro", "cuisine_type": "French"}
]

def print_restaurants():
    print("Restaurants:")
    for restaurant in restaurants:
        print(f"Name: {restaurant.get('name')}, Cuisine Type: {restaurant.get('cuisine_type')}")
