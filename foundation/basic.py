names = []

name = input("Enter name: ")

if name == "loser":
    names.append(name)

else:
    print("Good Job")

print(names)

fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")
