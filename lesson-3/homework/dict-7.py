dict1 = {"a" : 1,
         "b" : 2,
         "c" : 3}
key = "a"
if key in dict1:
    dict1.pop(key)
    print(dict1)
else:
    print("The key does not exist")