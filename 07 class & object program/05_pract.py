class first:
    salary = "200 $"

    @classmethod                        # A class method can access or modify the class state
    def funct(cls, sal):
        cls.salary = sal

    # def funct(self, sal):
    #     self.salary = sal

obj = first()

obj.funct("400 $")

print(f"Through class name value: {first.salary}")      # Class methods can be called by both class and object.
print(f"\nThrough object value: {obj.salary}")          # Class methods can be called by both class and object.
