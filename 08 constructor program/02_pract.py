class programmer:
    company = "Google"                                  # class attribute

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def putdata(self):
        print(f"\nProgrammer name: {self.name} and Programmer Id: {self.id}")

name = input("Enter the programmer name: ")
id = int(input("Enter the programmer id: "))

obj = programmer(name, id)
obj.putdata()