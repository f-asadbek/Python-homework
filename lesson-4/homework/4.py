import random
while True: 
	c = 0
	b = random.randint(1, 101)
	while c < 10: 
		a = int(input("Enter a number: "))
		if a == b :
			print("You guessed it right!")
			break
		elif a > b : 
			print("Too High!")
		else : 
			print("Too Low!")
			c += 1
	
	if c == 10 : 
		print("You lost. Want to play again?", b)
		d = input()
		if d in ("Y", "YES", "y", "yes", "ok") : 
			c = 0