a = 226

def funct():
    global a
    print(f"The value of global variable (a) in function: {a}")

    a = 20
    print(f"The value of global variable (a) after change in function: {a}")

funct()
print(f"The value of global varible (a): {a}")
