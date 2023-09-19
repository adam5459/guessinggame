#guessing game -by Adam S 
from random import randint
attempts = 0
ans = randint(1, 100)

def game():
    try :
        guess = int(input("Take a guess of the number (1 - 100)>  "))
    except ValueError:
        print("ERROR please only enter a integer")

    while guess != ans:
        try:
            if guess > 100:
                raise ValueError
            if guess > ans:
                guess = int(input("Your guess was highter than the aanswer. \n try again >   "))
            else:
                guess = int(input("Your guess was lower than the aanswer. \n try again >   "))
        except ValueError:
            print("Please only input integers")
    else:
        print("\nGood Job you win\n ")
        playAgain = input('Would you like to play again y/n? >  ')
    return playAgain.lower()

while game() == 'y':
    game()


