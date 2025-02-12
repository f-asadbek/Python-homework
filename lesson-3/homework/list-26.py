list1 = [1, 2, 3, 4, 5, 6, 7]
length = len(list1)
if length % 2 == 0:
    print(list1[length // 2 - 1], list1[length // 2])
else:
    print(list1[length // 2])