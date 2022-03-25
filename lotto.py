from random import randint


def get_user_number():
    while True:
        try:
            value = int(input())
            break
        except ValueError:
            print("It's not a number")
    return value


def user_list():
    user_nr = []
    while len(user_nr) < 6:
        print(f"Choose your number {len(user_nr)+1}: ")
        digit = get_user_number()
        if 0 < digit < 50:
            while digit in user_nr:
                print("The given number repeats, enter a different one")
                print(f"Choose your number {len(user_nr) + 1}: ")
                digit = get_user_number()
            user_nr.append(digit)
        else:
            print("You entered a number outside the 1-49 range, try again")

    user_nr.sort()
    return user_nr


def comp_list():
    list_nr = []
    for i in range(6):
        digit = randint(1, 49)
        while digit in list_nr:
            digit = randint(1, 49)
        list_nr.append(digit)
    list_nr.sort()
    return list_nr


def print_list(value):
    print("".join(str(value)))


def game():
    your_nr = user_list()
    print("You choose numbers:")
    print_list(your_nr)

    lotto_nr = comp_list()
    print("Lotto numbers:")
    print_list(lotto_nr)

    hits = 0
    for number in your_nr:
        if number in lotto_nr:
            hits += 1
    print(f"You hit {hits} {'number' if hits == 1 else 'numbers'}!")
    if hits > 2:
        print(f"Congratulations, You WIN!")
    else:
        print("Unfortunately, this time it did not work.")


if __name__ == '__main__':
    game()
    
