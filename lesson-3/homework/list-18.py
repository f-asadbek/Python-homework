def is_sublist(list1, list2):
    for i in range(len(list1) - len(list2) + 1):
        if list1[i : i + len(list2)] == list2:
            return True
    return False

list1 = [1, 2, 3, 4, 5]
list2 = [2 ,3]
if is_sublist(list1, list2):
    print("Sublist exists")
else:
    print("Sublist does not exist")