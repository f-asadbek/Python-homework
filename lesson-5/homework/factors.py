n = int(input("Enter a positive number: "))

if n > 0:
    for i in range(1, n + 1):
        if n % i == 0:
            print(f"{i} is a factor of {n}")
else:
    print("Invalid input")