programming_language = {
    'Python' : 'Guido van Rossum',
    'Java' : 'James Gosling',
    'C' : 'Dennis Ritchie',
    'Javascript' : 'Brendan Eich',
    'Ruby' : 'Yukihiro Matsumoto',
    'C#' : 'Anders Heijlsberg',
    'PHP' : 'Rasmus Lerdorf',
}

print("Programming Languages and their developers:", programming_language)

print("Developer of the 4th Programming Language:", programming_language['Javascript'])

programming_language['C#'] = 'Mads Torgersen'

del programming_language['Java']

print("Last key-value pair:", programming_language)