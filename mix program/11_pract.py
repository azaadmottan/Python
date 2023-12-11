print("Enter the value of a:",end="")
a = input()
print("Enter the value of b:",end="")
b = input()

try:
    print("The sum of two numbers is ",int(a) + int(b))
except Exception as e:
    print(e)
print("[a:",a,",b:",b,"]")