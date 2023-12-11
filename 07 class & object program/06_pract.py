class first:
    salary = 10000
    bonus = 2000

    @property                                           # getter method
    def total_salary(self):
        return self.salary + self.bonus
    
    @total_salary.setter                                # setter method 
    def total_salary(self, total):
        self.salary = total - self.bonus
        self.bonus = total - self.salary

obj = first()

# first.bonus = 4000
print(f"\nStarting (total salary): {obj.total_salary}, salary: {obj.salary} and bonus: {obj.bonus}")
# Through "property" method we can call function without paranthesis

obj.salary = 20000
print(f"\nTotal salary [when salary(20000)]: {obj.total_salary}, salary: {obj.salary} and bonus: {obj.bonus}")

obj.total_salary = 30000
print(f"\nWhen total salary is 30000 then, salary: {obj.salary} and bonus: {obj.bonus}")


