
names= ["Alice", "Bob", "Charlie"]

try:
    name = input("Enter name: ")
    names.append(name)

    print("Names list:", names)
except KeyboardInterrupt:
    print("\nYou typed Ctrl+C.")