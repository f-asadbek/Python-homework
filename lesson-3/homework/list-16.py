list = [1, 2, 3, 4, 5]
count = 0
for x in list:
    if x % 2 == 1:
        count += 1
print(f"There are {count} odd numbers in the list")