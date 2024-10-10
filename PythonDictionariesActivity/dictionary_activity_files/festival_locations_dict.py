festival_locations = {
    'Sinulog Festival' : 'Cebu City',
    'Ati-Atihan Festival' : 'Kalibo, Aklan',
    'Panagbenga Festival' : 'Baguio City',
    'Pahiyas Festival' : 'Lucban, Quezon',
    'Kadayawan Festival' : 'Davao City',
    'Masskara Festival' : 'Bago City, Negros Occidental',
    'Dinagyang Festival' : 'Iloilo City',
    'Higantes Festival' : 'Angono, Rizal',
}

print("Festival and their locations:", festival_locations)

print("Location of Pahiyas Festival:", festival_locations['Pahiyas Festival'])

festival_locations['Masskara Festival'] = 'Bacolod City'

del festival_locations['Ati-Atihan Festival']

print("Last key-value pair:", festival_locations)