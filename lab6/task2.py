# Функція для виконання операцій над списком
def list_operations(user_list):
    # Формуємо новий список, у який входить кожен другий елемент поточного списку
    new_list = user_list[1::2]  # Починаємо з другого елемента і крок 2

    return new_list


def main():
    # Введення списку з клавіатури
    user_input = input("Введіть елементи списку через пробіл: ")

    # Перетворення введених даних на список
    user_list = user_input.split()

    # Виклик функції для виконання операцій над списком
    new_list = list_operations(user_list)

    print(f"Новий список (кожен другий елемент): {new_list}")


if __name__ == "__main__":
    main()
