def file(filename):
    try:
        with open(filename, 'r') as f:
            print(f"{f.read()} (data)")
    except FileNotFoundError:
        print(f"{filename} is not found !")

file("pract_06_1.txt")
file("pract_06_3.txt")
file("pract_06_2.txt")