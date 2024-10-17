# Функція для обчислення середніх оцінок
def calculate_averages(grades):
    student_averages = {}
    total_sum = 0

    for student, scores in grades.items():
        # Обчислюємо середню оцінку для кожного учня
        average = sum(scores) / len(scores)
        student_averages[student] = average
        total_sum += average

    # Обчислюємо середню оцінку класу
    class_average = total_sum / len(grades)
    return student_averages, class_average


# Функція для виведення всіх значень словника
def display_grades(grades):
    print("Оцінки учнів:")
    for student, scores in grades.items():
        print(f"{student}: {scores}")


# Функція для додавання нового запису до словника
def add_student(grades, student, scores):
    grades[student] = scores
    print(f"Учня {student} додано зі списком оцінок {scores}.")


# Функція для видалення запису зі словника
def remove_student(grades, student):
    if student in grades:
        del grades[student]
        print(f"Учня {student} видалено.")
    else:
        print(f"Учня {student} не знайдено.")


# Функція для перегляду вмісту словника за відсортованими ключами
def display_sorted_students(grades):
    sorted_students = sorted(grades.keys())
    print("Учні у відсортованому порядку:")
    for student in sorted_students:
        print(f"{student}: {grades[student]}")


# Основна функція
def main():
    # Дані про оцінки учнів з n=10 учнів та 12 предметів
    grades = {
        "Петренко": [5, 6, 7, 8, 9, 10, 6, 7, 8, 9, 6, 5],
        "Савченко": [4, 5, 6, 7, 8, 5, 6, 7, 8, 9, 7, 6],
        "Крамар": [7, 7, 8, 8, 9, 9, 8, 7, 6, 5, 4, 5],
        "Коваленко": [10, 10, 9, 8, 7, 6, 5, 4, 5, 6, 7, 8],
        "Шевченко": [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
        "Остапенко": [3, 4, 5, 6, 3, 4, 5, 4, 3, 2, 1, 3],
        "Лисенко": [6, 7, 8, 9, 6, 7, 8, 9, 8, 7, 6, 5],
        "Гаценко": [9, 9, 8, 7, 6, 5, 4, 5, 6, 7, 8, 9],
        "Рубан": [10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9],
        "Братушка": [5, 6, 7, 8, 6, 7, 5, 6, 7, 8, 6, 5],
    }

    # Виведення всіх оцінок
    display_grades(grades)

    # Додавання нового учня
    add_student(grades, "Іваненко", [7, 8, 9, 6, 5, 7, 8, 7])

    # Видалення учня
    remove_student(grades, "Остапенко")

    # Відображення відсортованих учнів
    display_sorted_students(grades)

    # Обчислення середніх оцінок
    student_averages, class_average = calculate_averages(grades)
    print(f"\nСередня оцінка класу: {class_average:.2f}")

    # Виведення учнів з середньою оцінкою вище середньої по класу
    print("\nУчні з середньою оцінкою вище середньої по класу:")
    for student, average in student_averages.items():
        if average > class_average:
            print(f"{student}: {average:.2f}")


if __name__ == "__main__":
    main()
