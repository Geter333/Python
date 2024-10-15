def create_file(filename, lines):
    """Функція для створення текстового файлу та запису рядків."""
    try:
        with open(filename, 'w') as file:
            for line in lines:
                file.write(line + '\n')
        print(f"Файл {filename} створено успішно.")
    except Exception as e:
        print(f"Помилка при створенні файлу {filename}: {e}")


def process_files(file1, file2, file3):
    """Функція для переписування вмісту файла TF17_1 у TF17_2 з використанням допоміжного файла."""
    try:
        # Читаємо файл TF17_1
        with open(file1, 'r') as f1:
            content = f1.read()

        # Розділяємо цифри та інші символи
        digits = ''.join([char for char in content if char.isdigit()])
        others = ''.join([char for char in content if not char.isdigit() and char != '\n'])

        # Записуємо спочатку цифри, а потім інші символи в файл TF17_3
        with open(file3, 'w') as f3:
            f3.write(digits + others)

        # Читаємо з файла TF17_3 і записуємо у файл TF17_2 по 10 символів у рядку
        with open(file3, 'r') as f3, open(file2, 'w') as f2:
            data = f3.read()
            buffer = ''
            for char in data:
                buffer += char
                if len(buffer) == 10:  # Якщо в буфері 10 символів, записуємо їх у файл
                    f2.write(buffer + '\n')
                    buffer = ''
            if buffer:  # Записуємо залишкові символи (менше ніж 10) в кінці
                f2.write(buffer + '\n')

        print(f"Файл {file2} створено з використанням {file3}.")

    except FileNotFoundError as e:
        print(f"Файл не знайдено: {e}")
    except Exception as e:
        print(f"Помилка при обробці файлів: {e}")


def print_file_content(filename):
    """Функція для друку вмісту файлу по рядках."""
    try:
        with open(filename, 'r') as file:
            print(f"Вміст файла {filename}:")
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
    except Exception as e:
        print(f"Помилка при читанні файлу {filename}: {e}")


if __name__ == "__main__":
    # а) Створюємо файл TF17_1
    lines = ["Hello12345", "World6789", "Python3.10"]
    create_file('TF17_1.txt', lines)

    # б) Переписуємо вміст у файл TF17_2 через допоміжний TF17_3
    process_files('TF17_1.txt', 'TF17_2.txt', 'TF17_3.txt')

    # в) Читаємо і виводимо вміст файла TF17_2
    print_file_content('TF17_2.txt')
