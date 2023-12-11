class complex:

    def __init__(self, r, i):
        self.real = r
        self.imaginary = i

    def __add__(self, c_obj):
        return complex(self.real + c_obj.real, self.imaginary + c_obj.imaginary)
    
    def __mul__(self, c_obj):
        real = self.real * c_obj.real - self.imaginary * c_obj.imaginary
        imaginary = self.real * c_obj.imaginary + c_obj.real * self.imaginary

        return complex(real, imaginary)

    def __str__(self):
        return f"({self.real}) + i({self.imaginary})"

obj = complex(1, 2)
obj2 = complex(3, 4)

# sum = obj + obj2
print(f"First complex number  : {obj}")
print(f"Second complex number : {obj2}")
print("---------------------------------------")
print(f"Sum of two complex numbers are : {obj + obj2}")

obj3 = complex(2, -3)
obj4 = complex(3, 4)

print(f"\n\nFirst complex number  : {obj3}")
print(f"Second complex number : {obj4}")
print("---------------------------------------")
print(f"Multiplication of two complex numbers are : {obj3 * obj4}")

