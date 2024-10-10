movie_genres = {
    'Action' : 'Mad Max: Fury Road',
    'Comedy' : 'The Hangover',
    'Drama' : 'The Pursuit of Happyness',
    'Horror' : 'The Conjuring',
    'Science Fiction' : 'Inception',
    'Fantasy' : 'The Lord of the Rings',
    'Romantic Comedy' : '10 Things I Hate About You',
    'Animated' : 'Toy Story',
}

print("Movie genres and their example movies:", movie_genres)

print("Example movie of Drama:", movie_genres['Drama'])

movie_genres['Science Fiction'] = 'Interstellar'

del movie_genres['Romantic Comedy']

print("Last key-value pair:", movie_genres)