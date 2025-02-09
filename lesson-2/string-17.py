a = input("Enter a string: ")
symbol = "*"
b = "AEIOUaeiou"
result = ""

for char in a:
    if char in b:
        result += symbol
    else:
        result += char

print("Result:", result)
