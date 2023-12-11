num = int(input("Enter the value of num:"))

for i in range(1,11):
    print(f"{num} X {i} = {num * i}")


item = {'Sachin', 'Azaad', 'Rohit'}

for name in item:
    if name.startswith('S'):
        print("Hello",name)