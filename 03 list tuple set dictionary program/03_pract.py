dict = {
        "key" : "value",
        "c" : "procedural programming",
        "c++" : "Objected orinented programming",
        "Java" : "Pure object oriented programming",
        "list" : ["list data",20,"string"],
        "nested_dict" : {"nested" : "dictionary"}
}

print(type(dict))

print("\nDictionary data:",dict)

print("\nValue of c:",dict["c"])
print("\nValue of java:",dict['Java'])

print("\nValue of list in dictionary:",dict["list"])
print("\nValue of list in dictionary:",dict["list"])

print("\nValue of nested dictionary: ",dict["nested_dict"])
print("\nValue of nested dictionary data:",dict["nested_dict"]["nested"])

print("\nDictionary",dict.items())
print("\nKeys in dictionary:",dict.keys())
print("\nValue in dictionary:",dict.values())
print("\nlength of dictionary:",len(dict))
print("\nAccess item:",dict.get("Java"))