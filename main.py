#guessing game -by Adam S 
from random import randint
from sys import exit



def game():
    ans = randint(1, 100)
    attempts = 0
    max_attempts = 9
    try :
        emh = int(input('Would you like eas mediume or hard(1, 2 ,3)> '))
        if emh == 1:
            max_attempts = 14
        elif emh == 2:
            max_attempts = 9
        elif emh == 3:
            max_attempts = 4
        
        guess = int(input(f"Take a guess of the number (1 - 100) you have {max_attempts+1} gueses >  "))
        attempts +=1
    except  UnboundLocalError:
        print("ERROR please only enter a integer")

    except  ZeroDivisionError:
        print("ERROR please only enter a integer")

    except  ValueError:
        print("ERROR please only enter a integer")

    while guess != ans:
        if attempts > max_attempts:
            print('\n FAIL you took too many attempts \n')
            playAgain = input('Would you like to play again y/n? >  ')
            break

            
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


