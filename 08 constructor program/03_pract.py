class calculater:
    def __init__(self, num):
        self.number = num
    
    def square(self):
        print(f"\nThe square of {self.number} is {self.number ** 2}")

    def root(self):
        print(f"\nThe root of {self.number} is {self.number ** 0.5}")

    def cube(self):
        print(f"\nThe cube of {self.number} is {self.number ** 3}")

number = int(input("Enter number: "))

obj = calculater(number)

obj.square()
obj.root()
obj.cube()