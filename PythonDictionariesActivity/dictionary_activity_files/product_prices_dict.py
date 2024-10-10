product_prices = {
    '1 kg of Rice' : '₱40-₱60',
    '1 liter of gasoline' : '₱60-₱70',
    '500g of chicken breast' : '₱100-₱130',
    '1 dozen eggs' : '₱90-₱110',
    '1 kg of pork' : '₱250-₱300',
    '1 liter of milk' : '₱60-₱80',
    'Loaf of bread (500g)' : '₱50-₱70',
    '500ml bottled water' : '₱15-₱25',
    '1 kg of bananas' : '₱50-₱70',
    'Mobile phone (mid-range)' : '₱10,000-₱15,000',
}

print("Products and their prices:", product_prices)

print("Price of 1 dozen eggs:", product_prices['1 dozen eggs'])

product_prices['1 kg of bananas'] = '₱80'

del product_prices['1 liter of milk']

print("Last key-value pair:", product_prices)