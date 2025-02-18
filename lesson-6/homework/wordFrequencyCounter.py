import os
import string

def filteredText(text):
    return text.strip(string.punctuation).lower()
#///////////////////////////////////////////////////

def countWordFrequency(n = 5):
    if not os.path.exists("sample.txt"):
        text = input("Enter a text: ")
        with open("sample.txt", "a") as sample:
            sample.write(text)

    wordDict = {}
    with open("sample.txt", "r") as sample:
        for words in sample:
            lists = [filteredText(word) for word in words.split()]

    for word in lists:
        if word:
            wordDict[word] = wordDict.get(word, 0) + 1

    sorted_list = sorted(wordDict.items(), key=lambda x : x[1], reverse=True)

    print("Total words:", len(lists))
    print(f"Top {n} common words: ")
    for word, count in sorted_list[:n]:
        print(f"{word} - {count} times")

    with open("word_count_report.txt", "w") as word_count_report:
        word_count_report.write(f"Total words: {len(lists)} \n")
        word_count_report.write(f"Top {n} common words: \n")
        for word, count in sorted_list[:n]:
            word_count_report.writelines(f"{word} - {count}\n")

countWordFrequency()
#///////////////////////////////////////////////////

n = int(input("Enter a number: "))
countWordFrequency(n)