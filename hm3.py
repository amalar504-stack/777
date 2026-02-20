dictionary = {
    "hello": "привіт",
    "world": "світ",
    "book": "книга",
    "apple": "яблуко",
    "car": "автомобіль"
}

word = input("Введіть слово англійською: ").lower()

if word in dictionary:
    print("Переклад:", dictionary[word])
else:
    print("Слово не знайдено.")