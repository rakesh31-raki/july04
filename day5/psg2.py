import random
random_value = random.randint(1, 1000)
print(random_value)

i = 1


def guessme(guess_value, i):
    while i <= 10:
        try:
            user_value = int(input('enter : '))
            if user_value in range(1, 1000):
                if user_value == guess_value:
                    print("You got it right.. wow")
                    break
                else:
                    print("Guess another value")
            else:
                print("Entered value is in out of range")
        except ValueError as error:
            print("error")

        i += 1

    else:
        print("better luck next time")


guessme(random_value, i)
