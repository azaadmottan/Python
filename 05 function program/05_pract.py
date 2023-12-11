n = int(input("Enter the number: "))

def sum_natural(n):
    if(n == 0):
        return 0
    return sum_natural(n-1) + n

print(f"Sum of first {n} number is {sum_natural(n)}")