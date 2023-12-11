class First:
    publicVarible = 10                          # By default varibles are public 
    __privateVariable = 20                       # Private varibles are declared with "__" double underscore
    _protectedVariable = 30                      # Protected variables are declared with " _" single underscore



obj = First()

print(f"Public variable : {obj.publicVarible}")
print(f"Private variable : {obj._First__privateVariable}")
print(f"Protected variable : {obj._protectedVariable}")