student_grades = {
    'Addy' : 'B',
    'Bridget' : 'C',
    'Ianthe' : 'A',
    'Vaughn' : 'A+',
    'Ravi' : 'D',
}

print("Grades of Students:", student_grades)

print("Grade of the Third Student:", student_grades['Ianthe'])

student_grades['Bridget'] = 'D'

del student_grades['Ravi']

print("Last key-value pair:", student_grades)
