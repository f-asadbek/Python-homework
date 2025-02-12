list = [1, 2, 3, 4, 5]
count = 0
for x in list:
    if x % 2 == 0:
        count += 1
print(f"There are {count} even numbers in the list")