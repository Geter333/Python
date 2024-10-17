def unique_letters(text):
    # Створюємо словник для підрахунку кількості входжень кожної літери
    char_count = {}

    for char in text:
        if char.isalpha():  # Перевіряємо, чи є символ літерою
            char = char.lower()  # Опціонально: робимо текст нечутливим до регістру
            char_count[char] = char_count.get(char, 0) + 1

    # Формуємо множину літер, які зустрічаються лише один раз
    unique_chars = {char for char, count in char_count.items() if count == 1}

    return unique_chars


def main():
    user_input = input("Введіть текст з латинських літер: ")

    # Викликаємо функцію для пошуку літер, які зустрічаються лише один раз
    result_set = unique_letters(user_input)

    print(f"Літери, які входять в текст один раз: {result_set}")


if __name__ == "__main__":
    main()
