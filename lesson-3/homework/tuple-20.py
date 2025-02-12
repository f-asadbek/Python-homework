tuple1 = (1, 2, 3, 4, 5)
a = 2
tuple2 = ()
for i in range(0, len(tuple1), a) :
	tuple2 += (tuple1[i : i + a],)
print(tuple2)