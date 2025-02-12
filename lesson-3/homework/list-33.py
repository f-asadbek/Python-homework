list1 = [1, 2, 1, 3, 4, 1, 5]
element = 1
list2 = []
for x in range(len(list1)):
    if list1[x] == element:
        list2.append(x)
print(list2)