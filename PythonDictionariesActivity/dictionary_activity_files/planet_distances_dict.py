planet_distances = {
    'Mercury' : '57.9 million km',
    'Venus' : '108.2 million km',
    'Earth' : '149.6 million km',
    'Mars' : '227.9 million km',
    'Jupiter' : '777.4 million km',
    'Saturn' : '1,433.5 million km',
    'Uranus' : '2,872.5 million km',
    'Neptune' : '4,495.1 million km',
}

print("Planes and their distances from the Sun:", planet_distances)

print("Distance of Earth from the sun:", planet_distances['Earth'])

planet_distances['Jupiter'] = '778.5 million km'

del planet_distances['Uranus']

print("Last key-value pair:", planet_distances)