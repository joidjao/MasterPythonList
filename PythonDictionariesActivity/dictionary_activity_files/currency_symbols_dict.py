currency_symbols = {
    'US Dollars' : '$ (USD)',
    'Euro' : '€ (EUR)',
    'British Pound' : '£ (GBP)',
    'Japanese Yen' : '¥ (JPY)',
    'Philippine Peso' : '₱ (PHP)',
    'Canadian Dollar' : '$ (CAD)',
    'Australian Dollar' : '$ (AUD)',
    'Swiss Franc' : 'CHF',
    'Indian Rupee' : 'p (Paise)',
    'Chinese Yuan' : '¥ (CNY)',
}

print("Currencies and their symbols:", currency_symbols)

print("Symbol of Philippine Peso:", currency_symbols['Philippine Peso'])

currency_symbols['Indian Rupee'] = '₹ (INR)'

del currency_symbols['British Pound']

print("Last key-value pair:", currency_symbols)