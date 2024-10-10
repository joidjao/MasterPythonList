sports_events = {
    'FIFA World Cup' : 2022,
    'Summer Olympics' : 2021,
    'Super Bowl LVI' : 2022,
    'NBA Finals' : 2023,
    'Wimbledon Tennis Championship' : 2023,
    'Tour de France' : 2022,
    'UEFA Champions League Final' : 2023,
}

print("Sports events and their corresponding years:", sports_events)

print("Year of Super Bowl LVI:", sports_events['Super Bowl LVI'])

sports_events['Tour de France'] = 2023

del sports_events['Wimbledon Tennis Championship']

print("Last key-value pair:", sports_events)