number = [2,8,10,6,4]                                        # list methods 
print("List numbers are: ",number)

number.sort()
print("Sorted list are: ",number)

number.reverse()
print("Reversed list are: ",number)

print("Maximum number in list: ",max(number))

number.insert(2,12)
print("Inserted list are: ",number)
                                                     

tp_number = (2,4,6)                                         # Tuples
                                                            # Mutable can be change 
print("Tuple list are: ",tp_number)                         # Immutable cant't be change

a = 20
b = 40

print("The value of a & b before swap : ",a,b)

a,b = b,a

print("The value of a & b after swap : ",a,b)