city_landmarks = {
    'Paris, France' : 'Eiffel Tower',
    'New York City, USA' : 'Empire State Building',
    'Tokyo, Japan' : 'Tokyo Tower',
    'Rome, Italy' : 'Colosseum',
    'London, UK' : 'Tower Bridge',
    'Sydney, Australia' : 'Sydney Opera House',
    'Cairo, Egypt' : 'Pyramids of Giza',
    'Dubai, UAE' : 'Burj Khalifa',
}

print("Cities and their famous landmarks:", city_landmarks)

print("Landmark of Sydney, Australia:", city_landmarks)

city_landmarks['New York City, USA'] = 'Statue of Liberty'

del city_landmarks['Cairo, Egypt']

print("Last key-value pair:", city_landmarks)