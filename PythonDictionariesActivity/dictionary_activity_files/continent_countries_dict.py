continent_country = {
    'Asia' : 'China, India, Japan',
    'Africa' : 'Nigeria, Kenya, South Africa',
    'North America' : 'United States, Canada, Mexico',
    'Oceania' : 'Australia, New Zealand, Fiji',
    'South America' : 'Brazil, Argentina, Chile',
    'Europe' : 'Germany, France, Italy',
}

print("Continents and their 3 Countries:", continent_country)

print("Countries of the 4th Continent:", continent_country['Oceania'])

continent_country['South America'] = 'Colombia, Peru, Venezuela'

del continent_country['Europe']

print("Last key-value pair:", continent_country)