list = [2, 4, 6, 8]
print("Continue statement:",end = " " )

for item in list:
    if (item == 6):
        continue
    print(item,end=" ")

# Python uses the colon symbol (:) and indentation for showing where blocks of code begin and end.

list1 = [[2, 1, 3], [4, 3, 2], [6, 5, 4]]
print("\nNested lists:")
for item in list1:
    print(item)

print("Nested lists items:")
for item, item1, item2 in list1:
    print(item, item1, item2)

list3 = [1, 2, 3, [1, 2, 3], 4, 5]

# Nested lists are also valid in python. This means that a list can contain another list as an element.

print("Nested list elements:",end = " ")
print(list3[1],end = " ")
print(list3[3][2])
