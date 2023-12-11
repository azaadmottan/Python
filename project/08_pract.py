import os
import time
import colorama
from random import *
from colorama import Fore, Back, Style
colorama.init(autoreset = True)

os.system("cls")

password = input("Enter Password : ")

character = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
# character = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# character = ['0','1','2','3','4','5','6','7','8','9']

pwd = ""
while (pwd != password):
    pwd = ""
    for letter in range (len(password)):
        guess = character[randint(0, 35)]
        # guess = character[randint(0, 25)]
        # guess = character[randint(0, 9)]
        pwd = str(guess) + str(pwd)
        print(f"{Fore.RED}{pwd}")
        print(f"\n{Fore.BLUE}{Style.BRIGHT}Cracking Password.....")

        os.system("cls")

print(f"\n{Fore.GREEN}{Style.BRIGHT}Cracked Password !\n")

time.sleep(0.6)

print(f"{Fore.BLUE}{Style.BRIGHT}# Password : {Fore.RESET}{Fore.RED}{Style.BRIGHT}{pwd}\n")
