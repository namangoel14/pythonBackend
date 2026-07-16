# map(), filter() and reduce()

numbers = [1, 2, 3, 4, 5]

result = map(lambda x: x*2, numbers)
print(list(result))


filtering = filter(lambda x: x%2==0, numbers)
print(list(filtering))


num = [9, 7, 1, 5, 10, 88, 4]

outcome = sorted(num, reverse=True)
print("sorted: ", outcome)

string = ["Python", "Java", "Alice"]
print(sorted(string))

from functools import reduce

num = [1, 2, 3, 4, 5]

res = reduce(lambda a,b: a+b, num)
print(res)
