festival_dates = {
    'Sinulog Festival' : 'Third Sunday of January',
    'Ati-Atihan Festival' : 'Third Sunday of January',
    'Pahiyas Festival' : 'May 15',
    'Panagbenga Festival' : 'February',
    'Kadayawan Festival' : 'Third week of August',
    'Obando Fertility Rites' : 'May 17-19',
    'Festa ng Pagsanjan' : 'Last Sunday of January',
    'Bangus Festival' : 'April',
    'Hala Bira! Festival' : 'January 16-22',
    'National Mango Festival' : 'First week of April',
}

print("Festivals and their celebration dates:", festival_dates)

print("Celebration date of Pahiyas Festival:", festival_dates['Pahiyas Festival'])

festival_dates['Bangus Festival'] = 'Last week of April'

del festival_dates['Kadayawan Festival']

print("Last key-value pair:", festival_dates)