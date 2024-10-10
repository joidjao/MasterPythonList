car_brands = {
    'Toyota' : 'Japan',
    'Ford' : 'United States',
    'BMW' : 'Germany',
    'Ferrari' : 'Italy',
    'Hyundai' : 'South Korea',
    'Volvo' : 'Sweden',
    'Peugeot' : 'Spain',
    'Tata Motors' : 'India',
    'Chevrolet' : 'United States',
    'Volkswagen' : 'Germany',
}

print("Car brands and their country of origin:", car_brands)

print("Country of origin of 3rd Car brand:", car_brands['BMW'])

car_brands['Peugeot'] = 'France'

del car_brands['Tata Motors']

print("Last key-value pair:", car_brands)