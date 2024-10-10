flower = {
    'Rose' : 'Love',
    'Lily' : 'Purity',
    'Sunflower' : 'Adoration',
    'Cherry Blossom' : 'Beauty',
    'Tulip' : 'Elegance',
    'Daisy' : 'Innocence',
    'Orchid' : 'Strength',
    'Iris' : 'Hope',
}
print("Flowers and their symbolic meaning:", flower)

print("Symbolic meaning of Tulip:", flower['Tulip'])

flower['Orchid'] = 'Exotic Beauty'

del flower['Daisy']

print("Last key-value pair:", flower)