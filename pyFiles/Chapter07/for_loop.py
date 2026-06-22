l = [1, 7, 8]

for item in l:
    print(item)

print("\nNEW\n")

for itemRange in range(1,7):
    print(itemRange)


for item1 in range(0, 10, 2):
    if item1 == 4:
        continue
    print(item1)
else: 
    print("Loop is finally completed")

for item2 in range(0, 10, 2):
    if item2 == 6:
        break
    print(item2)


for j in range(1,9):
    pass


for i in 10:
    print(i)
