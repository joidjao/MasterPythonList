employees = [
    {"name": "Addy", "job_title": "Manager"},
    {"name": "Matcha", "job_title": "Developer"},
    {"name": "Sushi", "job_title": "Designer"},
    {"name": "Cheesecake", "job_title": "Marketing Specialist"},
    {"name": "Jo", "job_title": "Salesperson"}
]

def print_employees():
    print("Employees:")
    for employee in employees:
        print(f"Name: {employee.get('name')}, Job Title: {employee.get('job_title')}")