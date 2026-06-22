def count(n):
    if n<=0:
        print("Done!")
    else:
        print(n)
        count(n-1)
count(5)

def factorial(n):
    if n == 0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
