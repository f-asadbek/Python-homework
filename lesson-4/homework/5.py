a = input("Enter a passrowd: ")
if len(a) < 8 : 
	print("Password is too short.")
elif not any (b.isupper() for b in a) :
	print("Password must contain an uppercase letter.")
else : 
	print("Password is strong")