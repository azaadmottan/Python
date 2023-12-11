class first:
    def first(self):
        print("First class function !")

class second(first):                                    # multiple inheritance 
    def second(self):
        print("Second class function !")

class third(first):                                     # multiple inheritance 
    def third(self):
        print("Third class function !")

obj = second()
obj.first()
obj.second()

obj1 = third()
obj1.first()
obj1.third()