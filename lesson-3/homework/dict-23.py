dict1 = {"a" : 1,
         "b" : 2,
         "c" : 3}
dict2 = {"d" : 4,
         "e" : 5,
         "f" : 6}
if set(dict1.keys()).intersection(set(dict2.keys())):
    print(True)
else:
    print(False)