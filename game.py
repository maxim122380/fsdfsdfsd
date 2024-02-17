from random import choice
counter = 0
z = ["камень", "ножницы", "бумагу"]
player = input("Введите(бумага/камень/ножницы): ").lower()
y = choice(z)
print(f"Компьютер показал: {y}")

while counter != 3:
    if player == "камень" and y == "бумагу":
        print("Вы проиграли!")
    elif player == "камень" and y == "ножницы":
        print("Вы выиграли!")
        counter += 1
        print(f"Ваш счёт: {counter} очка.")
    elif player == "камень" and y == "камень":
        print("Ничья!")
    elif player == "ножницы" and y == "бумагу":
        print("Вы выиграли!")
        counter += 1
        print(f"Ваш счёт: {counter} очка.")
    elif player == "ножницы" and y == "ножницы":
        print("Ничья!")
    elif player == "ножницы" and y == "камень":
        print("Вы проиграли!")
    elif player == "бумага" and y == "бумагу":
        print("Ничья!")
    elif player == "бумага" and y == "ножницы":
        print("Вы проиграли!")
    elif player == "бумага" and y == "камень":
        print("Вы выиграли!")
        counter += 1
        print(f"Ваш счёт: {counter} очка.")

    else:
        print("Я вас не понял, введите ещё раз.")
    y = choice(z)
    player = input("Введите(бумага/камень/ножницы): ").lower()
    print(f"Компьютер показал: {y}")

print("Вы выиграли 3 раза, бот сдался!")