movie_directors = {
    'Dune' : 'Denis Villeneuve',
    'The Matrix Resurrection' : 'Lana Wachowski',
    'Free Guy' : 'Shawn Levy',
    'Blade Runner' : 'Denis Villeneuve',
    'Harry Potter' : 'J.K Rowling',
    'Annihilation' : 'Alex Garland',
    'Alita' : 'James Cameron',
    'Ad Astra' : 'James Gray',
    'The Midnight Sky' : 'Grant Heslov',
    'Arrival' : 'Denis Villeneuve',
}

print("Movies and their directors:", movie_directors)

print("Director of the 5th Movie:", movie_directors['Harry Potter'])

movie_directors['The Midnight Sky'] = 'George Clooney'

del movie_directors['Alita']

print("Last key-value pair:", movie_directors)
