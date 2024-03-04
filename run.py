import random

number_to_guess = random.randint(1, 10)

# print(number_to_guess)
count_number_tries = 1
guess = int(input('Please guess a number between 1 and 10: '))

while number_to_guess != to guess:
    print('Sorry, wrong number')
    # tbd
    if count_number_tries == 4:
        break
    elif guess < number_to_guess:
        print('The number is lower than your guess.')
    else:
        print('The number is higher than your guess')
        
    guess = int(input('Please guess again: '))
    count_number_tries += 1