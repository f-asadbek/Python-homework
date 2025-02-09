from datetime import datetime
a = input("Enter your name: ")
b = int(input("Enter your age: "))
print("Your birth year is", datetime.now().year - b)