dog = {
    'Chihuahua' : 'Small',
    'Pomeranian' : 'Small',
    'Beagle' : 'Medium',
    'Cocker Spaniel' : 'Medium',
    'Bulldog' : 'Medium',
    'Golden Retriever' : 'Large',
    'Labrador Retriever' : 'Large',
    'German Shepherd' : 'Large',
    'Rottweiler' : 'Large',
    'Great Dane' : 'Large',
}

print("Dog breeds and their sizes:", dog)

print(" Size of Bulldog:", dog['Bulldog'])

dog['German Shepherd'] = 'Medium'

del dog['Golden Retriever']

print("Last key-value pair:", dog)