coffee_types = {
    'Espresso' : 'Strong, concentrated coffee brewed by forcing hot water through finely-ground beans',
    'Cappuccino' : 'Equal parts espresso, steamed milk, and milk foam',
    'Latte' : 'Creamy, with a thin layer of foam on top',
    'Americano' : 'Espresso diluted with hot water',
    'Mocha' : 'Sweet and rich, often topped with whipped cream',
    'Macchiato' : 'Stronger than a latte but creamier than plain espresso',
    'Flat White' : 'More espresso-forward with less milk than a latte',
    'Cortado' : 'Equal parts espresso and steamed milk',
    'Affogato' : 'Both a coffee drink and a dessert',
    'Cold Brew' : 'Smooth, less acidic, and served chilled, often over ice',
}

print("Types of coffee and their descriptions:", coffee_types)

print("Description of the Americano:", coffee_types['Americano'])

coffee_types['Cortado'] = 'Balanced and smooth, without too much foam or froth'

del coffee_types['Mocha']

print("Last key-value pair:", coffee_types)