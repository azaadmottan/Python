import os
import random
import string
import time
import getpass

os.system("cls")

password = getpass.getpass("Enter password: ")
chars = string.ascii_lowercase + string.digits
guess = ''

while guess != password:
    guess = ''.join(random.sample(chars, len(password)))
    print("\r" + guess, end='')
    time.sleep(0.001)

print(f"\nPassword cracked: {guess}")
