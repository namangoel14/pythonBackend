
def main():
    try:
        num = int(input("Enter a number:"))
        return num
    except Exception as e:
        return e
    print("I am outside finally")
    finally:
        print("I am inside finally")

print(main())
