n = int(input("Enter the celsius temperature: "))

def funct(cel):
    return (cel * (9/5)) + 32

print(f"{n} degree celsius temperature is equal to {funct(n)}")