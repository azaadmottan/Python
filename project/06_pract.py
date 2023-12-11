import datetime
import os
import random
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset = True)

def game_win(comp, you):
    
    if(comp == you):
        return None

    elif(comp == 's'):
        if(you == 'w'):
            return False
        elif(you == 'g'):
            return True

    elif(comp == 'w'):
        if(you == 'g'):
            return False
        elif(you == 's'):
            return True 

    elif(comp == 'g'):
        if(you == 's'):
            return False
        elif(you == 'w'):
            return True

while(True):

    os.system("cls")
    
    print(f"\n{Fore.RED}{Style.BRIGHT}                       G  A  M  E                ")
    print(f"\n{Fore.YELLOW}{Style.BRIGHT}          (S N A K E,   W A T E R   &   G U N)                ")

    print(F"\n{Fore.LIGHTBLUE_EX}{Style.BRIGHT}Computer's turn {Fore.RESET}: Snake(s), Water(w) & Gun(g)    ====> ")
    you = input(f"\n{Fore.BLUE}{Style.BRIGHT}Your's turn {Fore.RESET}: Snake(s), Water(w) & Gun(g)        ====>{Fore.RED} ")

    rand = random.randint(1,3)

    if(rand == 1):
        comp = 's'
    elif(rand == 2):
        comp = 'w'
    elif(rand == 3):
        comp = 'g'

    print(f"{Fore.RESET}\nComputer choose ====> {Fore.GREEN}{comp}")
    print(f"\nYou choose      ====> {Fore.GREEN}{you}")

    result = game_win(comp, you)



    if(result == None):
        print(f"\n{Fore.YELLOW}{Style.BRIGHT}<----------    G A M E     T I E !    ---------->\n")
    elif(result == False):
        print(f"\n{Fore.RED}{Style.BRIGHT}<----------    Y O U     L O S E !    ---------->\n")
    elif(result == True):
        print(f"\n{Fore.BLUE}{Style.BRIGHT}<----------    Y O U     W I N !    ---------->\n")

    ans = input(f"\nType {Fore.RED}'EXIT'{Fore.RESET} for Quit the game Enter for 'Continue' the game! : ")
    if(ans == 'EXIT' or ans == 'exit'):
        break

    today_date_time = datetime.datetime.today()

    with open("06_pract_record_data.txt", 'a') as obj:
        if(result == None):
            obj.write(str(f'\n<----------    G A M E     T I E !    ---------->\t\t{today_date_time}'))
        elif(result == False):
            obj.write(str(f'\n<----------    Y O U     L O S E !    ---------->\t\t{today_date_time}'))
        elif(result == True):
            obj.write(str(f'\n<----------    Y O U     W I N !      ---------->\t\t{today_date_time}'))