import csv

def read_csv_file(filename):
    """Читає дані з CSV файлу та повертає їх як список словників."""
    data = []
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")
    return data


def search_data(data, country_name):
    """Шукає дані для заданої країни, ігноруючи регістр та пробіли."""
    results = []
    cleaned_country_name = country_name.strip().lower()  # Очищення назви країни
    for row in data:
        if row.get('Country Name', '').strip().lower() == cleaned_country_name:  # Ігноруємо регістр та пробіли
            results.append(row)
    return results


def write_to_csv_file(filename, data):
    """Записує результати пошуку у новий CSV файл."""
    if data:
        keys = data[0].keys()
        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=keys)
                writer.writeheader()
                writer.writerows(data)
            print(f"Результати записано у файл {filename}.")
        except Exception as e:
            print(f"Сталася помилка при запису у файл: {e}")
    else:
        print("Немає даних для запису.")


def main():
    input_filename = 'exports_data.csv'  # Вхідний файл з даними
    output_filename = 'results_data.csv'  # Вихідний файл для запису результатів

    # Читання даних з CSV файлу
    data = read_csv_file(input_filename)

    # Пошук даних за країнами
    while True:
        country_name = input("Введіть назву країни для пошуку (або 'exit' для виходу): ")
        if country_name.lower() == 'exit':
            break
        results = search_data(data, country_name)
        if results:
            print(f"Результати для '{country_name}':")
            for row in results:
                print(row)  # Виводимо знайдені дані в консоль
            write_to_csv_file(output_filename, results)
        else:
            print(f"Дані для країни '{country_name}' не знайдено.")


if __name__ == "__main__":
    main()
