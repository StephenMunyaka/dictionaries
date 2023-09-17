students = [
    {"name" : "Jane", "town": "Mombasa", "school": "TUM"},
    {"name": "Kelvin", "town": "Nairobi", "school": "UON"},
    {"name": "Susan", "town": "Kitale", "school": "PWANI"}
]
for student in students:
    print(student["name"], student["town"], student["school"], sep=",")