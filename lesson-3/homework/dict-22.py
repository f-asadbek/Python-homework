dict1 = {"c" : 1,
         "b" : 2,
         "a" : 3}
dict2 = {}
for key, value in dict1.items():
    if value > 0:
        dict2[key] = value
print(dict2)