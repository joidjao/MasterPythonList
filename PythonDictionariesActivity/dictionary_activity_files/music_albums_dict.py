music_albums = {
    'Thriller' : 1982,
    'The Dark Side of the Moon' : 1973,
    'Back in Black' : 1980,
    'Abbey Road' : 1969,
    'Lemonade' : 2016,
    'Nevermind' : 1991,
    'Rumours' : 1977,
    'The Wall' : 1978,
    '1989' : 2014,
    'Good Kid, M.A.A.D City' : 2012,
}

print("Music albums and their release years:", music_albums)

print("Release year of Back in Black:", music_albums['Back in Black'])

music_albums['The Wall'] = 1979

del music_albums['Lemonade']

print("Last key-value pair:", music_albums)