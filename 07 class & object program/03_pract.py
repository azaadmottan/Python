class first:
    def getdata(self):
        self.a = int(input("Enter the value of a:"))            # here " a " instance attribute
        self.b = int(input("Enter the value of b:"))            # here " b " instance attribute

    def putdata(self):
        print(f"\nThe value of a: {self.a}\nThe value of b: {self.b}")

    @staticmethod
    def funct():
        print("Hello World !")

obj = first()
obj1 = first()

obj.getdata()
obj1.getdata()

obj.funct()
obj.putdata()
obj1.putdata()