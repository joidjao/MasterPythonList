from dictionary_activity_files.space_missions_dict import space

space_telescope = {
    'Hubby Space Telescope' : 'Observed distant galaxies to measure the expansion rate of the universe',
    'James Webb Space Telescope' : 'Study the information of stars and planetary systems',
    'Chandra X-ray Observatory' : 'Study the supermassive black holes at the centers of galaxies',
    'Kepler Space Telescope' : 'Discover Earth-like exoplanets in the habitable zones of distant stars',
    'Spitzer Space Telescope' : 'Study the infrared emissions from distant galaxies and star-forming regions',
}

print("Spaces telescope and their missions:", space_telescope)

print("Misson of the Chandra X-ray Observatory:", space_telescope)

space_telescope['Hubby Space Telescope'] = 'Captured the iconic Pillars of Creation image in the Eagle Nebula'

del space_telescope['Kepler Space Telescope']

print("Last key-value pair:", space_telescope)