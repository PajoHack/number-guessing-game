import random


def play_game(): 

    number_to_guess = random.randint(1, 10)
    # print(number_to_guess)
    count_number_tries = 1

    def get_user_guess(prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print('Please enter a valid number between 1 and 10.')
                

    guess = get_user_guess('Please guess a number between 1 and 10: ')

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


def main():
    print(r"""

  ________                                  
 /  _____/ __ __   ____   ______ ______     
/   \  ___|  |  \_/ __ \ /  ___//  ___/     
\    \_\  \  |  /\  ___/ \___ \ \___ \      
 \______  /____/  \___  >____  >____  >     
        \/            \/     \/     \/      
  __  .__                                   
_/  |_|  |__   ____                         
\   __\  |  \_/ __ \                        
 |  | |   Y  \  ___/                        
 |__| |___|  /\___  >                       
           \/     \/                        
 _______               ___.                 
 \      \  __ __  _____\_ |__   ___________ 
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
\____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/    \/     \/       

    """)
    while True:
        play_game()
        play_again = input('Do you want to play again? (y/n): ').lower()
        if play_again != 'y':
            print('Thanks for playing!')
            break

if __name__ == "__main__":
    main()