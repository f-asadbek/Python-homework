set1 = {1, 2, 3}
element = 4
if element not in set1:
    set1.add(element)
    print(set1)
else:
    print("The element already exists in set")