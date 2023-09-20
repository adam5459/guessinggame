#guessing game -by Adam S 
from random import randint
from sys import exit



def game():
    ans = randint(1, 100)
    attempts = 0
    try :
        guess = int(input("Take a guess of the number (1 - 100) you have 10 gueses >  "))
        attempts +=1
    except  UnboundLocalError:
        print("ERROR please only enter a integer")

    except  ZeroDivisionError:
        print("ERROR please only enter a integer")

    except  ValueError:
        print("ERROR please only enter a integer")

    while guess != ans:
        if attempts > 9:
            print('\n FAIL you took too many attempts \n')
            exit()
        try:
            if guess > 100:
                raise ValueError
            if guess > ans:
                guess = int(input("Your guess was highter than the aanswer. \n try again >   "))
                attempts+=1
            else:
                guess = int(input("Your guess was lower than the aanswer. \n try again >   "))
                attempts+=1
        except ValueError:
            print("Please only input integers under 100")
            break
    else:
        print("\nGood Job you win\n ")
        playAgain = input('Would you like to play again y/n? >  ')
        attempts = 0 
    return playAgain.lower()
while game() == 'n':
  exit()
  
while game() == 'y':
    game()


