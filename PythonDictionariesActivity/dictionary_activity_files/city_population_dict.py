city_population = {
    'Manila' : 1850000,
    'Quezon' : 2960000,
    'Caloocan City' : 1660000,
    'Angeles City' : 462928,
    'San Fernando' : 354666,
    'Cebu City' : 1020000,
    'Pasig' : 803159,
    'Taguig' : 886722,
    'Davao City' : 1780000,
    'Antipolo' : 887399,
}

print("City population:", city_population)

print("Population of 6th City:", city_population['Cebu City'])

city_population['Caloocan City'] = 2770000

del city_population['Davao City']

print("Last key-value pair:", city_population)