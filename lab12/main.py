import json


# Функція для зчитування даних з JSON-файлу
def read_json_file(filename):
    with open(filename, "rt") as file:
        return json.load(file)


# Функція для запису даних у JSON-файл
def write_json_file(filename, data):
    with open(filename, "wt") as file:
        json.dump(data, file, indent=4)


# Виведення вмісту JSON-файлу
def display_json_content(filename):
    data = read_json_file(filename)
    for student in data["students"]:
        print(f"{student['Surname']} {student['Name']}, Оцінки: {student['Grades']}")


# Додавання нового запису в JSON-файл
def add_student(filename, surname, name, grades):
    data = read_json_file(filename)
    new_student = {"Surname": surname, "Name": name, "Grades": grades}
    data["students"].append(new_student)
    write_json_file(filename, data)
    print(f"Додано учня: {surname} {name}")


# Видалення запису з JSON-файлу за прізвищем
def remove_student(filename, surname):
    data = read_json_file(filename)
    data["students"] = [student for student in data["students"] if student["Surname"] != surname]
    write_json_file(filename, data)
    print(f"Видалено учня з прізвищем: {surname}")


# Пошук записів у JSON-файлі за прізвищем або ім'ям
def search_student(filename, field, value):
    data = read_json_file(filename)
    results = [student for student in data["students"] if student.get(field) == value]
    if results:
        for student in results:
            print(f"Знайдено: {student['Surname']} {student['Name']}, Оцінки: {student['Grades']}")
    else:
        print(f"Записів з {field} = {value} не знайдено.")


# Обчислення середньої оцінки учня
def calculate_average(grades):
    return sum(grades) / len(grades)


# Обчислення середньої оцінки кожного учня і середньої оцінки по класу
def calculate_class_averages(filename, output_filename):
    data = read_json_file(filename)

    for student in data["students"]:
        student["Average"] = calculate_average(student["Grades"])

    class_average = sum(student["Average"] for student in data["students"]) / len(data["students"])
    print(f"\nСередня оцінка по класу: {class_average:.2f}")

    high_average_students = [
        {"Surname": student["Surname"], "Name": student["Name"], "Average": student["Average"]}
        for student in data["students"] if student["Average"] > class_average
    ]

    # Зберегти результат у новий JSON-файл
    output_data = {
        "students": data["students"],
        "class_average": class_average,
        "high_average_students": high_average_students
    }
    write_json_file(output_filename, output_data)

    # Виведення результатів
    print("\nСередня оцінка кожного учня:")
    for student in data["students"]:
        print(f"{student['Surname']} {student['Name']}: {student['Average']:.2f}")

    print("\nУчні з середньою оцінкою вище за середню по класу:")
    for student in high_average_students:
        print(f"{student['Surname']} {student['Name']}: {student['Average']:.2f}")


# Головне меню програми
def main():
    filename = "students_grades.json"
    output_filename = "students_results.json"

    while True:
        print("\nМеню:")
        print("1. Вивести вміст JSON-файлу")
        print("2. Додати нового учня")
        print("3. Видалити учня")
        print("4. Пошук учня за полем")
        print("5. Розрахувати середню оцінку по класу і зберегти результат")
        print("6. Вийти")

        choice = input("Оберіть дію: ")

        if choice == "1":
            display_json_content(filename)
        elif choice == "2":
            surname = input("Введіть прізвище: ")
            name = input("Введіть ім'я: ")
            grades = list(map(int, input("Введіть оцінки через пробіл: ").split()))
            add_student(filename, surname, name, grades)
        elif choice == "3":
            surname = input("Введіть прізвище учня для видалення: ")
            remove_student(filename, surname)
        elif choice == "4":
            field = input("Введіть поле для пошуку (Surname або Name): ")
            value = input("Введіть значення для пошуку: ")
            search_student(filename, field, value)
        elif choice == "5":
            calculate_class_averages(filename, output_filename)
        elif choice == "6":
            print("Програма завершена.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


# Запуск програми
main()

