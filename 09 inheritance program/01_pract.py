class base:                                     # base class or parent class or super class 

    @staticmethod
    def base_funct():
        print("\nBase class function !")
                                                # single inheritance relation
class derive(base):                             # derive class or child class or sub class

    @staticmethod
    def derive_funct():
        print("\nDerive class function !")

obj = derive()

obj.base_funct()
obj.derive_funct()