country_capital = {
    'Philippines' : 'Manila',
    'Japan' : 'Tokyo',
    'South Korea' : 'Seoul',
    'Thailand' : 'Bangkok',
    'North Korea' : 'Pyongyang',
    'Australia' : ' Canberra',
    'Germany' : 'Berlin',
    'France' : 'Marseille',
    'Unites States' : 'Washington, D.C',
    'Canada' : 'Ottawa',
    'Brazil' : 'Brasilia',
    'Russia' : 'Moscow',
}

print("Country Capitals:", country_capital)

print("Capital of the 5th Country:", country_capital['North Korea'])

country_capital['France'] = 'Paris'

del country_capital['Brazil']

print("Last key-value pair:", country_capital)