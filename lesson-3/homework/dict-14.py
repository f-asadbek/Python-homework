dict1 = {"a" : 1,
         "b" : 2,
         "c" : 3}
a = 2
list1 = []
for key, value in dict1.items():
    if value == a:
        list1.append(key)
print(list1)