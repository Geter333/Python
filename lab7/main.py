# Функція для обчислення середніх оцінок
def calculate_averages(grades):
    # Обчислення середньої оцінки для кожного учня
    student_averages = {}
    total_sum = 0

    for student, scores in grades.items():
        average = sum(scores) / len(scores)
        student_averages[student] = average
        total_sum += average

    # Обчислення середньої оцінки класу
    class_average = total_sum / len(grades)

    return student_averages, class_average


def main():
    # Дані про оцінки учнів
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

    # Обчислення середніх оцінок
    student_averages, class_average = calculate_averages(grades)

    print(f"Середня оцінка класу: {class_average:.2f}\n")
    print("Середні оцінки учнів:")

    for student, average in student_averages.items():
        print(f"{student}: {average:.2f}")

    print("\nУчні з середньою оцінкою вище середньої в класі:")

    for student, average in student_averages.items():
        if average > class_average:
            print(f"{student}: {average:.2f}")


if __name__ == "__main__":
    main()
