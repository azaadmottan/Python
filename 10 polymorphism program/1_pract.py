class operator_overloading:
    def __init__(self, x):
        self.num = x
        print(f"\nThe value of x:",self.num)
    
    def __add__(self, obj):
        return self.num + obj.num
    
    def __sub__(self, obj):
        return self.num - obj.num
    
    def __mul__(self, obj):
        return self.num * obj.num

    def __truediv__(self, obj):
        return self.num / obj.num

obj1 = operator_overloading(10)
obj2 = operator_overloading(20)

sum = obj1 + obj2                                                           # overload " + " operator
print(f"\nSum of {obj1.num} and {obj2.num} : {sum}")

subt = obj1 - obj2                                                          # overload " - " operator
print(f"Subtraction of {obj1.num} and {obj2.num} : {subt}")

mult = obj1 * obj2                                                          # overload " * " operator
print(f"Multiplication of {obj1.num} and {obj2.num} : {mult}")

divis = obj1 / obj2                                                         # overload " / " operator
print(f"Division of {obj1.num} and {obj2.num} : {divis}")