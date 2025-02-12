tuple1 = (1, 2, 3, 4, 5, 1)
tuple2 = ()
for i in tuple1 : 
	if tuple1.count(i) == 1 :
		tuple2 += (i,)
print(tuple2)