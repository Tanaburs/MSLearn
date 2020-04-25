import random
number = 0
guess = 1
tries = 0

while guess != number:
    number = random.randint(1, 5)
    tries += 1
    input("Guess a number between 1 and 5: ")

print(f'You guess it in {tries} tries!')
