tuple1 = (1, 2, 3, 4, 5)
element = 3
list1 = list(tuple1)
list1.remove(element)
tuple1 = tuple(list1)
print(tuple1)