car_specs = {
    'Toyota Corolla Altis' : 'Engine: 1.6L 4-cylinder, 121 hp, gasoline',
    'Honda Civic' : 'Engine: 1.5L turbocharged 4-cylinder, 180 hp, gasoline',
    'Ford Ranger' : 'Engine: 2.0L Bi-Turbo 4-cylinder, 210 hp, diesel',
    'Mitsubishi Montero Sport' : 'Engine: 2.4L 4-cylinder, 181 hp, diesel',
    'Nissan Terra' : 'Engine: 2.5L 4-cylinder, 187 hp, diesel',
    'Hyundai Tucson' : 'Engine: 2.0L 4-cylinder, 154 hp, gasoline',
    'Mazda 3' : 'Engine: 2.0L 4-cylinder, 153 hp, gasoline',
    'Chevrolet Trailblazer' : 'Engine: 1.3L turbocharged 3-cylinder, 155 hp, gasoline',
    'Suzuki Ertiga' : 'Engine: 1.5L 4-cylinder, 103 hp, gasoline',
    'Subaru Forester' : 'Engine: 2.0L 4-cylinder, 156 hp, gasoline',
}

print("Car models and their engine specifications:", car_specs)

print("Specification of Mitsubishi Montero Sport:", car_specs['Mitsubishi Montero Sport'])

car_specs['Suzuki Ertiga'] = '1.5L K15B, 4-cylinder, DOHC 16-valve'

del car_specs['Nissan Terra']

print("Last key-value pair:", car_specs)