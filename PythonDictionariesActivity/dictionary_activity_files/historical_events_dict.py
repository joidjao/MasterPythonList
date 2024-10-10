historical = {
    'Arrival of Ferdinand Magellan' : 1521,
    'Philippine Revolution against Spain' : 1896,
    'Declaration of Philippine Independence' : 'June 12, 1898',
    'Philippine-American War' : 1899-1902,
    'Japanese Occupation of the Philippines' : 1942-1945,
    'Post-War Independence' : 'July 4, 1946',
    'Martial Law Declaration by Ferdinand Marcos' : 'September 22, 1972',
    'People Power Revolution (EDSA Revolution)' : 'February 22-25, 1986',
}

print("Historical events and their years:", historical)

print("Year of Philippine Revolution against Spain:", historical['Philippine Revolution against Spain'])

historical['Martial Law Declaration by Ferdinand Marcos'] = 'September 21, 1972'

del historical['Japanese Occupation of the Philippines']

print("Last key-value pair:", historical)