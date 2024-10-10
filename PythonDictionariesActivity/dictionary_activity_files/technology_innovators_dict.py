technology_inventors = {
    'Personal Computer' : 'Bill Gates',
    'Internet' : 'Tim Berners-Lee',
    'Smartphone' : 'Steve Jobs',
    'Electric Car' : 'Elon Musk',
    'Artificial Intelligence' : 'John McCarthy',
    'Blockchain' : 'Satoshi Nakamoto',
    'Social Media Platforms' : 'Mark Zuckerberg',
    'Cloud Computing' : 'Jeff Bezos',
}

print("Technologies and their innovations:", technology_inventors)

print("Innovator of Electric Car:", technology_inventors['Electric Car'])

technology_inventors['Internet'] = 'Vint Cerf'

del technology_inventors['Blockchain']

print("Last key-value pair:", technology_inventors)