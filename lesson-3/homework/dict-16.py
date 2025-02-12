dict1 = {"a" : 1,
         "b" : 2,
         "c" : 3,
        "d" : {"e" : 4}}
nested = any(isinstance(value, dict) for value in dict1.values())
print(nested)