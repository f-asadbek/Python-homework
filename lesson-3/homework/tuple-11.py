tuple1 = (1, 2, 1, 3, 1, 4, 1, 5)
element = 1
list1 = []
for i in range(len(tuple1)):
    if tuple1[i] == element:
        list1.append(i)
print(list1)