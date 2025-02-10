a = input("Enter a sentence: ")
b = input("Enter a word you want to replace on your sentence: ")
c = input("Enter a word you want to replace with: ")
if b in a:
    print("Output:", a.replace(b, c))
else:
    print("Entered word is not in a sentence")