company = {
    'Ayala Corp.' : 'Jaime Ayala',
    'SM Corp.' : 'Frederick Go',
    'Jollibee' : 'Jose Magsaysay Jr.',
    'Meralco' : 'Ray Espinosa',
    'PLDT Inc.' : 'Alfredo Panlilio',
    'Globe Telecom' : 'Ernesr Cu',
    'Ayala Lanc, Inc.' : 'Bobby Dy',
    'San Miguel Corp.' : 'Ramon Ang',
    'Aboitiz Power Corp.' : 'Antonio Aboitiz',
    'Union Bank' : 'Edwin Bautista',
}

print("Companies and their current CEO", company)

print("CEO of Globe Telecom:", company['Globe Telecom'])

company['Jollibee'] = 'Ernesto Tanmantiong'

del company['Aboitiz Power Corp.']

print("Last key-value pair:", company)
