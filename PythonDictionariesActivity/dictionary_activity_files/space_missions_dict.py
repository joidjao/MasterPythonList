space = {
    'Apollo 11' : 1969,
    'Voyager 1' : 1976,
    'Hubby Space Telescope' : 1990,
    'Mars Rover Curiosity' : 2012,
    'Perseverance Rover' : 2021,
}

print("Space missions and years:", space)

print("Year of Hubby Space Telescope:", space['Hubby Space Telescope'])

space['Voyager 1'] = 1977

del space['Mars Rover Curiosity']

print("Last key-value pair", space)