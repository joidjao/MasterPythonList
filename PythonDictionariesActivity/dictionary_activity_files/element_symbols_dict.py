element_symbols = {
    'Hydrogen' : 'H',
    'Helium' : 'He',
    'Oxygen' : 'O',
    'Carbon' : 'C',
    'Nitrogen' : 'N',
    'Iron' : 'Fe',
    'Gold' : 'Au',
    'Silver' : 'S',
    'Sodium' : 'Na',
    'Calcium' : 'Ca',
}

print("Elements and their Chemical Symbols:", element_symbols)

print("Symbol of the 6th element:", element_symbols['Iron'])

element_symbols['Silver'] = 'Ag'

del element_symbols['Sodium']

print("Last key-value pair:", element_symbols)