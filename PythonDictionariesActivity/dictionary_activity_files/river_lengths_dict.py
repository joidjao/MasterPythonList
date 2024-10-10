river = {
    'Cagayan River' : '505 km',
    'Mindanao River' : '373 km',
    'Agusan River' : '349 km',
    'Pulangi River' : '320 km',
    'Pampanga River' : '259 km',
    'Abra River' : '178 km',
}

print("Rivers and their length kilometers:", river)

print("Length of Mindanao River:", river['Mindanao River'])

river['Pampanga River'] = '260 km'

del river['Pulangi River']

print("Last key-value pair:", river)