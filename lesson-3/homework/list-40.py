list1 = [1, 2, 3, 2, 4, 5, 4]
list2 = []
for x in list1:
    if list1.count(x) == 1:
        list2.append(x)
print(list2)