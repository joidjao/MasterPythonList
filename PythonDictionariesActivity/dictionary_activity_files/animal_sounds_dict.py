animal_sounds = {
    'Cats' : 'Meow',
    'Dogs' : 'Arff',
    'Pigs' : 'Oink',
    'Cow' : 'Moo',
    'Duck' : 'Quack',
    'Frog' : 'Kokak',
    'Chicken' : 'Kookkorokoo',
    'Sheep' : 'Meeeh',
}

print("Animal sounds:", animal_sounds)

print("Sound of the 4th animal:", animal_sounds['Cow'])

animal_sounds['Chicken'] = 'Cluck'

del animal_sounds['Duck']

print("Last key-value pair:", animal_sounds)