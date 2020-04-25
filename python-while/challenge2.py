import random
number = random.randint(1, 10)
count = 0
guess = 0


while guess != number:
    count += 1
    guess = input(f'Enter guess #{count}: ')

    if guess.isnumeric():
        guess = int(guess)
    else:
        print('Numbers only, please!')
        continue
    if guess > number:
        print('Your guess is too high, try again!')
    elif guess < number:
        print('Your guess is too low, try again!')

else:
    print(f'You guessed it in {count} tries!')




