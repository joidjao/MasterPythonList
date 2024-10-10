state_capital = {
    'California' : 'Sacramento',
    'Texas' : 'Austin',
    'Florida' : 'Tallahassee',
    'New York' : 'Albany',
    'Illinois' : 'Springfield',
    'Ohio' : 'Columbus',
    'Pennsylvania' : 'Harrisburg',
    'Michigan' : 'Lansing',
    'Georgia' : 'Savannah',
    'Colorado' : 'Denver',
}

print("States and their capitals:", state_capital)

print("Capital of New York:", state_capital)

state_capital['Georgia'] = 'Atlanta',

del state_capital['Pennsylvania']

print("Last key-value pair:", state_capital)