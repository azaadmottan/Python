class value:                                                            # create class 
    a = 10    # by default class member are public                      # class data members
    b = 20    # class attribute                                         # class data members

    def putdata(self):                                                  # class member function
        print(f"The value of a: {self.a}\nThe value of b: {self.b}")


obj = value()                                                           # create object of class (value)

obj.putdata()                                                           # invoke class member function (putdata)
