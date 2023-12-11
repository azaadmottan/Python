n = int(input("Enter the number: "))

def fibonacci(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("Fibonacci series: ",end="")
for i in range(0,n):
    print(fibonacci(i),end=" ")