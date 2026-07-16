dict1 = {"a":1, "b":2}
dict2 = {"b":3, "c":4}
merged = dict1 | dict2
print("With or(|) operator:",merged)

dict1.update(dict2)
print("With update():", dict1)

dict1 |= dict2
print("With |= operator:",dict1)
