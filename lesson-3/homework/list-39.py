list1 = [1, 2, 3, 4, 5, 6]
list2 = []
a = 3
for x in range(0, len(list1), a):
    list2.append(list1[x : x + a])
print(list2)