n = int(input("Enter the number: "))

prime = True
for i in range(2, n):
    if(n % i == 0):
        prime = False

if(prime == True):
    print(f"{n} is prime number")
else:
    print(f"{n} is not prime number")