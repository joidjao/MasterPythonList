plant_types = {
    'Rose' : 'Shrub',
    'Fern' : 'Non-flowering plant',
    'Cactus' : 'Succulent',
    'Bamboo' : 'Grass',
    'Mango Tree' : 'Evergreen',
    'Lavender' : 'Herb',
    'Oak Tree' : 'Deciduous Tree',
    'Water Lily' : 'Aquatic Plant',
}

print("Plants and their types:", plant_types)

print("Type of Mango tree:", plant_types['Mango Tree'])

plant_types['Fern'] = 'Pteridophyte'

del plant_types['Lavender']

print("Last key-value pair:", plant_types)