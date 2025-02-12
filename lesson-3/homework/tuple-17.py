tuple1 = (1, 2, 3, 4, 5)
tuple2 = (1, 2, 3)
if set(tuple2).issubset(tuple1):
    print(max(tuple2))
else:
    print("no")