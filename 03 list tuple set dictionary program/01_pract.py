list_1 = [20,20.44,"string value",True,4+6j]
print("\nList 1 data:",list_1)                                  # List operation

print("\nlength of string:",len(list_1))

list_1.reverse()
print("\nReversed list:",list_1)

list_2 = [30,4,60,50]
print("\nList 2 data:",list_2)
list_1.append(list_2)
print("\nAppend list:",list_1)

poped = list_1.pop(3)
list_1.remove(4+6j)
print("\npoped element:",poped)
# list_1.remove(True)
list_1.remove("string value")
print("\nRemoved and poped list:",list_1)

list_3 = [100,80,70,90]
print("\nList 3 data:",list_3)
list_2.extend(list_3)
print("\nExtend list:",list_2)

list_2.insert(8,200)
print("\nInserted list:",list_2)

list_2.sort()
print("\nSorted list:",list_2)

print("\nLargest element:",max(list_2))
print("\nSmallest element:",min(list_2))

print("\nList data using for loop: ",end=' ')
for i in list_2:
    print(i,end=' ')

print("\n\nAccess index of list data: ",end=' ')
for i in list_2:
    print(list_2.index(i),end=' ')

list_converson = tuple(list_2)
print("\n\nList converted into tuple:",list_converson)
