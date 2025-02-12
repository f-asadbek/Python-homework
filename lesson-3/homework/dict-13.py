dict1 = {"a" : 1,
         "b" : 2,
         "c" : 3}
dict2 = dict(zip(dict1.values(), dict1.keys()))
print(dict2)