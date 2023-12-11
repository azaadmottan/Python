def square(a):
    return a * a

print("Enter a number to find square: ")
a = int(input())

result = square(a)
print("Square of",a,"is",result)

# recursion 
def recursion(b):
    if(b == 0 or b ==1):
        return 1
    else:
        return b * recursion(b-1)

def iterative(n):
    fact = 1
    for i in range(n):
        fact = fact * (i + 1)
    return fact
print("Enter a number you to have to find factorial: ")
b = int(input())

ans1 = recursion(b)
print("Factorial of",b,"using recursion is",ans1)
ans2 = iterative(b)
print("Factorial of",b,"using iterative is",ans2)
