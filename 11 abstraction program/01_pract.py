from abc import ABC, abstractclassmethod

class A(ABC):

    @abstractclassmethod
    def funct(self):
        print("Abstract function")

class B(A):
    
    def funct2(self):
        print("class B funct2 invoked")
        
    def funct(self):
        print("Abstract function")

# obj = A()                   # we can't create object of abstract class 

obj = B()
obj.funct()