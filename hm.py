contacts = {}

while True:
    print("\n1 - Додати")
    print("2 - Видалити")
    print("3 - Змінити")
    print("4 - Показати всі")
    print("0 - Вийти")

    choice = input("Ваш вибір: ")

    if choice == "1":
        name = input("Ім'я: ")
        phone = input("Телефон: ")
        contacts[name] = phone
        print("Додано!")

    elif choice == "2":
        name = input("Ім'я для видалення: ")
        if name in contacts:
            contacts.pop(name)
            print("Видалено!")
        else:
            print("Не знайдено!")

    elif choice == "3":
        name = input("Ім'я для зміни: ")
        if name in contacts:
            phone = input("Новий телефон: ")
            contacts[name] = phone
            print("Змінено!")
        else:
            print("Не знайдено!")

    elif choice == "4":
        if len(contacts) == 0:
            print("Контактів немає.")
        else:
            for name in contacts:
                print(name + ": " + contacts[name])

    elif choice == "0":
        break

    else:
        print("Невірний вибір!")