import pandas as pd

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

df = pd.DataFrame(grades)

print("DataFrame:\n", df)

print("\nБали студента Рубан:\n", df["Рубан"])

print("\nСереднє значення оцінок Рубан =", df["Рубан"].mean())

print("Сума оцінок Рубан =", df["Рубан"].sum())

print("Мінімальна оцінка Рубан =", df["Рубан"].min())

print("Максимальна оцінка Рубан =", df["Рубан"].max())
