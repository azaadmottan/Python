class base:
    def __init__(self):
        print("Base class constructor !")

class derive_1(base):                                                           # multilevel inheritance
    def __init__(self):
        super().__init__()
        print("Derive 1 class constructor !")

class derive_2(derive_1):                                                       # multilevel inheritance
    def __init__(self):
        super().__init__()
        print("Derive 2 class construcor !")

obj = derive_2() 
