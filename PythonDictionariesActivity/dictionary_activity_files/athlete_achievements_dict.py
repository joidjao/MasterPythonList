athletes = {
    'Manny Pacquiao' : 'First and only boxer to win world titles in eight different weight divisions',
    'Hidilyn Diaz' : 'First Filipino to win an Olympic gold medal (weightlifting, Tokyo 2020)',
    'Paeng Nepomuceno' : 'Guinness World Record holder for most bowling titles, with 133 career titles',
    'Efren Reyes' : 'Widely regarded as one of the greatest pool players of all time, winning multiple world championships, including the WPA World Nine-ball Championship (1999)',
    'Lydia de Vega' : 'Asias fastest woman in the 1980s, winning multiple gold medals in the Asian Games and Southeast Asian Games in track and field',
    'Carlos Yulo' : 'First Filipino to win a gold medal at the World Artistic Gymnastics Championships (2019, floor exercise)',
    'Eugene Torre' : 'Asias first chess grandmaster, achieving the title in 1974',
    'Margielyn Didal' : 'Gold medalist in skateboarding at the 2018 Asian Games and a finalist at the Tokyo 2020 Olympics',
}

print("Athletes and their greatest achievements:", athletes)

print("Achievement of Lydia de Vega:", athletes['Lydia de Vega'])

athletes['Paeng Nepomuceno'] = 'World Bowling Cup'

del athletes['Eugene Torre']

print("Last key-value pair:", athletes)