class University:
    def __init__(self, name, location):
        self.name = name
        self.location = location

university_name_list = ["University of the Philippines Diliman", "Ateneo de Manila University", "De La Salle University", "University of Santo Tomas", "University of San Carlos"]
university_location_list = ["Quezon City", "Quezon City", "Manila", "Manila", "Cebu City"]

print("\nUniversity Data:")
for i in range(len(university_name_list)):
    print(f"Name: {university_name_list[i]}, Location: {university_location_list[i]}")
