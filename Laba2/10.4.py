message = input("Введите сообщение: ")
i = 0
for letter in message:
    try:
        m = message[i + 1]
    except IndexError:
        print(letter)
    i += 1
