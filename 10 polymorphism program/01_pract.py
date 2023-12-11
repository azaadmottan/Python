class A:
    var1 = 10
    var2 = 20

    def __init__(self):
        print("Class A constructor invoked\n")
    
    def funct1(self):
        print("Class A funct1 invoked\n")

    def funct2(self):
        print("Class A funct2 invoked\n")

class B(A):
    var1 = 30
    var2 = 40

    def __init__(self):
        super().__init__()                                      # class "A" constructor invoked first
        print("Class B constructor invoked\n")

    def funct1(self):
        print("Class B funct1 invoked\n")
        super().funct1()

    def funct2(self):
        print("Class B funct2 invoked\n")


# obj = A()
obj1 = B()


obj1.funct1()
# obj1.funct2()

# obj.funct1()
# obj.funct2()