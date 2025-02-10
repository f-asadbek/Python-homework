a = input("Enter string: ")
vowels = "aeiouAeiou"
vowel = 0
consonant = 0
for char in a:
    if char.isalpha():
        if char in vowels:
            vowel += 1
        else:
            consonant += 1
print("Vowels:", vowel)
print("Consonants:", consonant)