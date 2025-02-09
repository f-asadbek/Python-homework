a = input("Enter a string: ")
if any(b.isdigit() for b in a):
    print("There is a digit")
else:
    print("There is not a digit")