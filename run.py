import random

number_to_guess = random.randint(1, 10)
print(number_to_guess)
count_number_tries = 1

guess = int(input('Please guess a number between 1 and 10: '))

while number_to_guess != guess:
    print('Sorry, wrong number.')

    if count_number_tries == 4:
        break
    elif guess < number_to_guess:
        print('Go higher!')
    else:
        print('Go lower!')
        
    guess = int(input('Please guess again: '))
    count_number_tries += 1
    
    
if number_to_guess == guess:
    print('Well done you won!')
    print('You took', count_number_tries, 'goes to complete the game')
else:
    print('Sorry - you loose')
    print('The number you needed to guess was', number_to_guess)
