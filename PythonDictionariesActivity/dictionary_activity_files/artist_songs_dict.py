artist = {
    'Sarah Geronimo' : 'Tala',
    'Regine Velasquesz' : 'Kailangan Ko Ay Ikaw',
    'Ben&Ben' : 'Pagtingin',
    'Eraserheads' : 'Ang Huling El Bimbo',
    'Moira Dela Torre' : 'Malaya',
    'Parokya ni Edgar' : 'Harana',
    'Gary Valenciano' : 'Hanggang Sa Dulo ng Walang Hanggan',
    'IV of Spades' : 'Mundo',
}

print("Artists and their top Songs:", artist)

print("Top song of Ben&Ben:", artist['Ben&Ben'])

artist['Parokya ni Edgar'] = 'Buloy'

del artist['Gary Valenciano']

print("Last key-value pair:", artist)