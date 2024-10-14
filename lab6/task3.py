# Функція для виконання операцій над множинами
def unique_letters(text):
    # Перетворюємо текст на множину символів
    char_set = set(text)

    # Створюємо словник для підрахунку кількості входжень кожного символу
    char_count = {}

    for char in text:
        if char.isalpha():  # Перевіряємо, чи є символ літерою
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    # Створюємо множину символів, які зустрічаються лише один раз
    unique_chars = {char for char, count in char_count.items() if count == 1}

    # Перевіряємо, чи є унікальні символи
    if len(unique_chars) == 0:
        # Якщо немає унікальних символів, перетворюємо множину на список і назад
        return set(list(char_set))

    return unique_chars


def main():
    user_input = input("Введіть текст з латинських літер: ")

    # Виклик функції для виконання операцій над множинами
    result_set = unique_letters(user_input)

    print(f"Літери, які входять в текст один раз: {result_set}")


if __name__ == "__main__":
    main()
