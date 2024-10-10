animal_habitats = {
    'Elephant' : 'Forest',
    'Polar Bear' : 'Arctic Sea Ice',
    'Dolphin' : 'Oceans',
    'Kangaroo' : 'Grasslands',
    'Penguin' : 'Antarctic Ice',
    'Frog' : 'Lakes',
    'Tiger' : 'Grasslands',
    'Eagle' : 'Mountains',
}

print("Animals and their Habitats:", animal_habitats)

print("Habitat of the 3rd Animal:", animal_habitats['Dolphin'])

animal_habitats['Penguin'] = 'Coastal Regions'

del animal_habitats['Tiger']

print("Last key-value pair:", animal_habitats)