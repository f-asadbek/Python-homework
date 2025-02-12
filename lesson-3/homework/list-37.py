list1 = [1, 2, 3, -4, -5]
sum = int(0)
for x in list1:
    if x < 0:
        sum += x
print("Sum of negative numbers:", sum)