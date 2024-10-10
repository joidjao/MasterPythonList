company_founders = {
    'Jollibee' : 'Tony Tan Caktiong',
    'SM' : 'Felicidad Sy',
    'San Miguel Corp.' : 'Enrique Maria Barretto de Ycaza',
    'GMA' : 'Robert Stewart',
    'Ayala' : 'Domingo Roxas',
    'PLDT' : 'Ramon Cojuangco',
    'Globe Telecom' : 'Henry Herman Sr.',
    'National Book Store' : 'Socorro Ramos',
}

print("Companies and their Founders:", company_founders)

print("Founder of PLDT:", company_founders['PLDT'])

company_founders['SM'] = 'Henry Sy. Sr'

del company_founders['National Book Store']

print("Last key-value pair:", company_founders)