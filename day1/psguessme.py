import random


def guess_me(max_chance=10):
    chance = 1
    rand_value = random.randint(1, 1000)

    while chance <= max_chance:
        try:
            prompt = f'Chance : {chance}\nenter the value :'
            user_value = int(input(prompt))
        except ValueError:
            print('invalid input, retrying....\n')
            continue

        if user_value == rand_value:
            print('you won :) !!!!!!!')
            break
        elif user_value > rand_value:
            print(f'{user_value}: greater')
        else:
            print(f'{user_value}: lesser')

        chance += 1
        print()
    else:
        print('you lost :(.....')
        print()

guess_me()