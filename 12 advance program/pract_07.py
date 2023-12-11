def funct(num):
    # print(num)
    return lambda a : num * a

number = funct(2)
print(number(3))