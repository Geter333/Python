sentence = "Це приклад речення з різними словами, це речення демонстраційне."
words = set(sentence.lower().replace(",", "").replace(".", "").split())
print("Унікальні слова в реченні:", words)
