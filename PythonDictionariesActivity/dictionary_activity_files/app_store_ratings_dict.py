app_store = {
    'Facebook' : 4.1,
    'Instagram' : 4.5,
    'WhatsApp' : 4.3,
    'YouTube' : 4.4,
    'TikTok' : 4.4,
    'Spotify' : 4.5,
    'Google Maps' : 4.3,
    'Gmail' : 4.2,
    'Zoom' : 4.3,
    'Netflix' : 4.3,
}

print("Apps and their ratings:", app_store)

print("Ratings of Spotify:", app_store['Spotify'])

app_store['Gmail'] = 4.3

del app_store['Zoom']

print("Last key-value pair:", app_store)