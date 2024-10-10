food_recipes = {
    'Spaghetti Carbonara' : 'Pasta, eggs, Parmesan cheese, bacon, garlic, olive oil',
    'Beef Caldereta' : 'Beef, tomato sauce, liver spread, potatoes, carrots, bell peppers, spices',
    'Chicken Adobo' : 'Chicken, soy sauce, vinegar, garlic, bay leaves, peppercorns, oil',
    'Pork Sinigang' : 'Pork, tamarind soup base, tomatoes, radish, spinach, green beans',
    'Fish Tacos' : 'White fish fillets, tortillas, cabbage slaw, lime, salsa',
    'Garlic Butter Shrimp' : 'Shrimp, garlic, butter, lemon juice, parsley',
    'Stir-Fried Tofu with Vegetables' : 'Tofu, bell peppers, broccoli, soy sauce, garlic, sesame oil',
    'Scrambled Eggs'  : 'Eggs, butter, salt, pepper',
}

print("Foods and their recipes:", food_recipes)

print("Recipe of Fish Tacos:", food_recipes['Fish Tacos'])

food_recipes['Chicken Adobo'] = 'Simmer chicken with soy sauce, vinegar, and spices until tender'

del food_recipes['Stir-Fried Tofu with Vegetables']

print("Last key-value pair:", food_recipes)