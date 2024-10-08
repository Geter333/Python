word = "обробка_рядків_у_Python"  # Можна змінити на будь-яке інше слово

underscore_count = word.count('_')

if underscore_count > 0:
    print(f"У слові є {underscore_count} символ(и) '_'.")
else:
    print("Символів '_' у слові немає.")
