class Employee:

    def data(self):       # self is used for when function invoke through any object "self" replace by object name
        return f"Name : {self.name}\nId : {self.id}\nRole : {self.role}\n"

obj = Employee()

obj.name = "Azaad Mottan"
obj.id = 235689
obj.role = "Programmer"
print(obj.data())

obj2 = Employee()

obj2.name = "Sachin Kumar"
obj2.id = 123456
obj2.role = "Software Developer"
print(obj2.data())
