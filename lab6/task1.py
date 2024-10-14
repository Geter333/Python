# Функція для операцій над списком
def list_operations(user_list):
    # Перевертання списку
    reversed_list = user_list[::-1]

    # Визначення кількості елементів у списку
    length_of_list = len(user_list)

    return reversed_list, length_of_list


def main():
    # Введення списку з клавіатури
    user_input = input("Введіть елементи списку через пробіл: ")

    # Перетворення введених даних на список
    user_list = user_input.split()

    # Виклик функції для виконання операцій над списком
    reversed_list, length_of_list = list_operations(user_list)

    # Виведення результатів
    print(f"Список у зворотньому порядку: {reversed_list}")
    print(f"Кількість елементів у списку: {length_of_list}")


if __name__ == "__main__":
    main()
