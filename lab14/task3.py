import json
import matplotlib.pyplot as plt

# Завантаження даних з JSON-файлу
with open('students_grades.json', 'r') as file:
    students = json.load(file)

# Обчислення середніх оцінок
average_grades = [sum(student["Grades"]) / len(student["Grades"]) for student in students]
labels = [f"{student['Surname']} {student['Name']}" for student in students]

# Побудова кругової діаграми
plt.figure(figsize=(10, 8))
plt.pie(average_grades, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Середні оцінки студентів')
plt.axis('equal')  # Щоб діаграма була круглою
plt.show()
