universities = [
    {"name": "University of the Philippines", "location": "Quezon City, Metro Manila"},
    {"name": "Ateneo de Manila University", "location": "Quezon City, Metro Manila"},
    {"name": "De La Salle University", "location": "Manila, Metro Manila"},
    {"name": "University of Santo Tomas", "location": "Manila, Metro Manila"},
    {"name": "Mapúa University", "location": "Intramuros, Manila"}
]

def print_universities():
    print("Universities:")
    for university in universities:
        print(f"Name: {university.get('name')}, Location: {university.get('location')}")
