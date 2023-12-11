obj = open('01_pract.txt', 'r')
# obj = open('01_pract.txt')       # Bu default mode is 'r'

file_data = obj.read()

print("File data:",file_data)

obj.close()