list1 = [1, 2, 3, 4, 5]

b = [item for item in list1 if item % 2 == 0]                   # list comprehension 

print(b)

dict1 = {i:f"{i}" for i in range(1, 100) if i % 2 == 0}         # dictionary comprehension
print(dict1)