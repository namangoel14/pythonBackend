#from typing import Dict
age: int = 27

def greeting (name: str) -> str:
    return f"Hello {name}"

print(greeting(age))


jsonValue: dict[str, int] = {
        "age": 27
        }
print(jsonValue)

listValue: list[int] = [1, 2, 3, 4, 5]

print(listValue)

tupleValue: tuple[str, int] = ("Naman", 27)
print(tupleValue)
unionValue: int | str = 25
print(unionValue)


