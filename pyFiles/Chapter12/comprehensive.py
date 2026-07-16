list1 = [1, 2, 3, 4, 5]

list2 = [item*item for item in list1 if len(list1) > 4]
print(list2)
