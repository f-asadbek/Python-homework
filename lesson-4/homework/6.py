for i in range(1, 101) :
	is_prime = True
	if i < 2: 
		continue
	for j in range(2, int(i ** 0.5) + 1):
		if i % j == 0 :
			is_prime = False
			break
	if is_prime : 
		print(i, " ")