set1 = {1, 2, 3, 4, 5}
set2 = set()
for i in set1:
    if i % 2 == 0:
        set2.add(i)
print(set2)