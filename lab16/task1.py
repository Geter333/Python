import nltk
import string
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

try:
    file = open('milton-paradise.txt', 'r', encoding='utf-8')
except FileNotFoundError:
    print("Файл не знайдено!")
    exit(0)

text = file.read()


# Функція для підрахунку кількості слів у тексті
def count_words(text):
    sentences = nltk.sent_tokenize(text)  # Токенізація по реченням
    word_count = 0
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)  # Токенізація по словах
        word_count += len(words)
    return word_count


# Функція для визначення найбільш вживаних слів
def most_used_words(text):
    words = text.split()
    word_count = Counter(words)
    most_common = word_count.most_common(10)

    # Побудова стовпчастої діаграми
    x = [item[0] for item in most_common]
    y = [item[1] for item in most_common]
    plt.bar(x, y)
    plt.title("10 найбільш вживаних слів у тексті")
    plt.xlabel("Слова")
    plt.ylabel("Кількість повторень")
    plt.show()


# Функція для очищення тексту від стоп-слів та пунктуації
def clean_text(text):
    words = word_tokenize(text)  # Токенізація
    words = [word.lower() for word in words if word.isalpha()]  # Видалення пунктуації та перетворення в нижній регістр
    stop_words = set(stopwords.words('english'))  # Завантаження стоп-слів
    filtered_words = [word for word in words if word not in stop_words]  # Видалення стоп-слів
    return filtered_words


cleaned_text = clean_text(text)

cleaned_word_count = len(cleaned_text)
print(f"Кількість слів після очищення: {cleaned_word_count}")


# Підрахунок найбільш вживаних слів після очищення
def cleaned_most_used_words(text):
    words = clean_text(text)
    word_count = Counter(words)
    most_common = word_count.most_common(10)

    x = [item[0] for item in most_common]
    y = [item[1] for item in most_common]
    plt.bar(x, y)
    plt.title("10 найбільш вживаних слів після очищення")
    plt.xlabel("Слова")
    plt.ylabel("Кількість повторень")
    plt.show()


word_count = count_words(text)
print(f"Кількість слів у тексті: {word_count}")
most_used_words(text)
cleaned_most_used_words(text)
