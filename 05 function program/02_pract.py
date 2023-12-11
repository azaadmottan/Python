n = int(input("Enter the number: "))

def fact(n):
    if(n == 0 or n == 1):
        return 1
    return n * fact(n-1)

print(f"Factorial of {n} is {fact(n)}")