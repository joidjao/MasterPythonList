class Employee:
    def __init__(self, name, job_title):
        self.name = name
        self.job_title = job_title

employee_name_list = ["Addy", "Matcha", "Sushi", "Cheesecake", "Jo"]
employee_job_title_list = ["Manager", "Developer", "Designer", "Analyst", "Salesperson"]

print("\nEmployee Data:")
for i in range(len(employee_name_list)):
    print(f"Name: {employee_name_list[i]}, Job Title: {employee_job_title_list[i]}")
