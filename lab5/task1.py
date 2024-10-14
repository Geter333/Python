# Введення масиву з клавіатури
n = int(input("Введіть кількість елементів масиву: "))  # Запитуємо кількість елементів
array = []

print("Введіть елементи масиву:")
for i in range(n):
    element = float(input(f"Елемент {i + 1}: "))  # Запитуємо кожен елемент масиву
    array.append(element)

# Обчислення середнього арифметичного додатніх елементів
positive_elements = [x for x in array if x > 0]  # Фільтрація тільки додатніх елементів

if len(positive_elements) > 0:
    average_positive = sum(positive_elements) / len(positive_elements)  # Обчислення середнього
    print(f"Середнє арифметичне додатніх елементів: {average_positive}")
else:
    print("У масиві немає додатніх елементів.")
