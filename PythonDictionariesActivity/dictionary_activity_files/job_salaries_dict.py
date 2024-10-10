job_salary = {
    'Software Developer' : '₱300,000 - ₱600,000 per year',
    'Data Analyst' : '₱240,000 - ₱500,000 per year',
    'Civil Engineer' : '₱240,000 - ₱480,000 per year',
    'Teacher' : '₱200,000 - ₱350,000 per year',
    'Registered Nurse' : '₱250,000 - ₱480,000 per year',
    'Accountant' : '₱220,000 - ₱450,000 per year',
    'Marketing Manager' : '$75,000 - $130,000 per year',
    'Graphic Designer' : '₱180,000 - ₱400,000 per year',
    'Human Resources Manager' : '₱300,000 - ₱650,000 per year',
    'IT Support Specialist' : '₱200,000 - ₱450,000 per year',
}

print("Jobs and their average salaries:", job_salary)

print("Salary of Civil Engineer:", job_salary)

job_salary['Marketing Manager'] = '₱350,000 - ₱700,000 per year'

del job_salary['Human Resources Manager']

print("Last key-value pair:", job_salary)