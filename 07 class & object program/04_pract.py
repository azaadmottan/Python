class first:
    def getdata(self, id1, name1):
        self.id = id1
        self.name = name1

    def putdata(self):
        print(f"\nId: {self.id}\nName: {self.name}")

obj = first()

obj.getdata(21072, "Azaad mottan")               # passing paremeters to class member function(getdata)
obj.putdata()

obj.id = 2107264
obj.name = "Sachin Kumar"

obj.putdata()

# first.id = 2107246                                # we can change class attribute value
# print(first.id)
# obj.putdata()
del obj
