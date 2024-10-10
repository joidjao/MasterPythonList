fruit_colors = {
    'Apple' : 'Red',
    'Banana' : 'Yellow',
    'Grapes' : 'Purple',
    'Orange' : 'Green',
    'Blueberry' : 'Blue',
    'Cherry' : 'Red',
    'Blackberry' : 'Black',
    'Peach' : 'Pink',
}

print("Fruits and their corresponding colors:", fruit_colors)

print("Color of the 6th Fruit:", fruit_colors['Cherry'])

fruit_colors['Orange'] = 'Orange'

del fruit_colors['Blackberry']

print("Last key-value pair:", fruit_colors)