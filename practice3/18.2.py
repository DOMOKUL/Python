def ask_password():
    i = 0
    password = "password"

    while True:
        s = input()
        i += 1
        if s == password and i <= 3:
            print("Пароль принят")
            i += 3

        elif i == 3:
            print("В доступе отказано")
