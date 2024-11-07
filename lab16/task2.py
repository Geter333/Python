import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer
import string

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

try:
    file = open('text.txt', 'r', encoding='utf-8')
except FileNotFoundError:
    print("Файл не знайдено!")
    exit(0)

text = file.read()

words = word_tokenize(text)

# Створення об'єктів для лемматизації та стеммінгу
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

# Видалення стоп-слів і пунктуації
stop_words = set(stopwords.words('english'))
punctuation = set(string.punctuation)

# Лемматизація, стеммінг, видалення стоп-слів і пунктуації
processed_words = []
for word in words:
    if word.lower() not in stop_words and word not in punctuation:
        # Лемматизація
        lemmatized_word = lemmatizer.lemmatize(word)
        # Стеммінг
        stemmed_word = stemmer.stem(lemmatized_word)
        processed_words.append(stemmed_word)

with open("processed_text.txt", "w", encoding="utf-8") as file:
    file.write(" ".join(processed_words))

print("Оброблений текст:")
print(" ".join(processed_words))
