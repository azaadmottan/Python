ans = lambda a, b : a+b

def funct(n):
    return lambda a : a * n

p = funct(2)
print("Double of given number:",p(4))

x = int(input("Enter the value of x:"))
y = int(input("Enter the value of y:"))
print("Sum of",x,"and",y,"is",ans(x,y))