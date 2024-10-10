beaches_countries = {
    'White Beach' : 'Boracay Island, Philippines',
    'Bondi Beach' : 'Sydney, Australia',
    'Copacabana Beach' : 'Rio de Janeiro, Brazil',
    'Waikiki Beach' : 'Honolulu, US',
    'Anse Source d Argent' : 'La Digue Island, Seychelles',
    'Maya Bay' : 'Phi Phi Islands, Thailand',
    'Grace Bay Beach' : 'Providenciales Island, Turks and Caicos Islands',
    'Navagio Beach' : 'Zakynthos Island, Greece',
}

print("Beaches and the Countries they are located:", beaches_countries)

print("Country of Copacabana Beach:", beaches_countries['Copacabana Beach'])

beaches_countries['Maya Bay'] = 'Krabi, Thailand'

del beaches_countries['Anse Source d Argent']

print("Last key-value pair:", beaches_countries)