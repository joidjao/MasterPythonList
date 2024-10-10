university_courses = {
    'UP' : 'Political Science',
    'ADMU' : 'Law',
    'DLSU' : 'Accountancy',
    'UST' : 'Medicine',
    'USC' : 'Engineering',
    'MP' : 'Information Technology',
    'FEU' : 'Nursing',
    'PUP' : 'Accountancy',
}

print("Universities and their popular courses:", university_courses)

print("Course of the 3rd University:", university_courses['DLSU'])

university_courses['USC'] = 'Business'

del university_courses['FEU']

print("Last key-value pair:", university_courses)