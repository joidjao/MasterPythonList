holiday = {
    'New Years Day' : 'January 1',
    'All Souls Day' : 'November 2',
    'Ninoy Aquino Day' : 'August 21',
    'All Saints Day' : 'November 1',
    'New Years Eve' : 'December 31',
    'Rizal Day' : 'December 30',
    'Christmas Day' : 'December 25',
    'Labor Day' : 'May 1',
    'Bonifacio Day' : 'November 29',
    'Araw ng Kagitingan' : 'April 9',
}

print("Holidays and their corresponding dates:", holiday)

print("Date of All Saints Day:", holiday['All Saints Day'])

holiday['Bonifacio Day'] = 'November 30'

del holiday['All Souls Day']

print("Last key-value pair:", holiday)