video_game = {
    'The Legend of Zelda' : 'Nintendo Switch',
    'Red Dead Redemption 2' : 'PlayStation',
    'Fortnite' : 'Xbox',
    'Minecraft' : 'PlayStation',
    'The Witcher 3' : 'PC',
    'Grand Theft Auto V' : 'PlayStation',
    'Animal Crossing' : 'Nintendo',
    'Call of Duty' : 'PlayStation',
}

print("Video games and their platforms:", video_game)

print("Platform of Red Dead Redemption 2:", video_game['Red Dead Redemption 2'])

video_game['Grand Theft Auto V'] = 'Xbox'

del video_game['Minecraft']

print("Last key-values pair:", video_game)