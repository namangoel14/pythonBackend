
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is to long ({n} elements, expected <= 3)")

if name := input("Enter the name: "):
    print(f"Hello {name}")

while (num := int(input("Enter a number:"))) != 0:
    print(num)
else:
    print(f"You hit the {num}")

string = "Naman"
if (length := len(string)) >= 5:
    print(f"{length}")
