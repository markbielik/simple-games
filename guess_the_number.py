from random import randint


def user_number():
    while True:
        try:
            user_nr = int(input("Gess the number: "))
            break
        except Exception:
            print("It's not number!")
    return user_nr


def game():
    search_nr = randint(1, 100)
    your_nr = user_number()
    while your_nr != search_nr:
        if your_nr < search_nr:
            print("To small")
        else:
            print("To big")
        your_nr = user_number()
    print("Great, You WIN!")


if __name__ == '__main__':
    game()