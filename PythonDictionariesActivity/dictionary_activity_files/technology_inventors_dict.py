technology = {
    'Telephone' : 'Alexander Graham Bell',
    'Light Bulb' : 'Thomas Edison',
    'Airplane' : 'Orville Wright',
    'World Wide Web' : 'Tim Berners-Lee',
    'Electric Motor' : 'Michael Faraday',
    'Radio' : 'Nikola Tesla',
}

print("Technologies and their Inventors", technology)

print("Inventor of World Wide Web:", technology['World Wide Web'])

technology['Light Bulb'] = 'Joseph Swan'

del technology['Radio']

print("Last key-value pair:", technology)