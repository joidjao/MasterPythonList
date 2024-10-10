class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

restaurant_name_list = ["Italian Bistro", "Sushi Place", "Steakhouse", "Vegan Delights", "Taco Haven"]
restaurant_cuisine_type_list = ["Italian", "Japanese", "American", "Vegan", "Mexican"]

print("\nRestaurant Data:")
for i in range(len(restaurant_name_list)):
    print(f"Name: {restaurant_name_list[i]}, Cuisine Type: {restaurant_cuisine_type_list[i]}")
