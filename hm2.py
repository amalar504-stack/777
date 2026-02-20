rates = {"USD": 40.2, "EUR": 42.5, "PLN": 9.6}

currency = input("Валюта (USD, EUR, PLN): ").upper()
amount = float(input("Сума в гривнях: "))

if currency in rates:
    result = amount / rates[currency]
    print("Результат:", round(result, 2), currency)
else:
    print("Такої валюти немає.")