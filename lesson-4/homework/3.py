txt = input("Enter a String: ")
count = 0
vowels = "AEIOUaeiou"
result = ""
for i in range(len(txt)): 
	count += 1
	result += txt[i]
	if count >= 3 and i != len(txt) - 1 and txt[i] not in vowels:
		vowels += txt[i]
		result += "_"
		count = 0
print(result)