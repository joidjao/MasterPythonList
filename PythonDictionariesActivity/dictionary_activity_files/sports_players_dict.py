sports_players = {
    'Soccer' : 'Lionel Messi',
    'Basketball' : 'Michael Jordan',
    'Tennis' : 'Roger Federer',
    'Cricket' : 'Sachin Tendulkar',
    'Golf' : 'Tiger Woods',
    'Football' : 'Tom Brady',
    'Baseball' : 'Babe Ruth',
    'Ice Hockey' : 'Wayne Gretzky',
    'Formula 1' : 'Michael Schumacher',
    'Rugby' : 'Richie McCaw',
}

print("Sports and their most famous players:", sports_players)

print("Player of the 4th sport:", sports_players['Cricket'])

sports_players['Football'] = 'Joe Montana'

del sports_players['Rugby']

print("Last key-value pair:", sports_players)