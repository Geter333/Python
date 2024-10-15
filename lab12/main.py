import json

students = [
    {"Surname": "Ivanov", "Name": "Ivan", "Grades": [9, 8, 10, 7, 8]},
    {"Surname": "Petrov", "Name": "Petr", "Grades": [6, 7, 8, 6, 7]},
    {"Surname": "Sidorov", "Name": "Sidor", "Grades": [10, 9, 8, 9, 10]},
    {"Surname": "Kovalenko", "Name": "Olena", "Grades": [7, 7, 8, 6, 7]},
    {"Surname": "Shevchenko", "Name": "Taras", "Grades": [5, 5, 6, 5, 6]},
    {"Surname": "Bondarenko", "Name": "Anna", "Grades": [8, 8, 7, 9, 8]},
    {"Surname": "Tkachenko", "Name": "Mykola", "Grades": [7, 8, 9, 7, 8]},
    {"Surname": "Melnyk", "Name": "Andriy", "Grades": [6, 6, 7, 6, 6]},
    {"Surname": "Krivenko", "Name": "Oksana", "Grades": [9, 9, 8, 9, 9]},
    {"Surname": "Gavriluk", "Name": "Dmytro", "Grades": [7, 6, 8, 7, 6]}
]

# Записуємо дані в JSON файл
json_data = json.dumps(students)
with open("students_grades.json", "wt") as file:
    file.write(json_data)

# Читаємо дані з JSON файлу
with open("students_grades.json", "rt") as file:
    students = json.loads(file.read())

# Функція для обчислення середньої оцінки
def calculate_average(grades):
    return sum(grades) / len(grades)

# Обчислення середньої оцінки кожного учня
for student in students:
    student["Average"] = calculate_average(student["Grades"])

# Обчислення середньої оцінки по класу
class_average = sum(student["Average"] for student in students) / len(students)

print("Середня оцінка кожного учня:")
for student in students:
    print(f"{student['Surname']} {student['Name']}: {student['Average']:.2f}")

print(f"\nСередня оцінка по класу: {class_average:.2f}")

print("\nУчні з середньою оцінкою вище за середню по класу:")
for student in students:
    if student["Average"] > class_average:
        print(f"{student['Surname']} {student['Name']}: {student['Average']:.2f}")
