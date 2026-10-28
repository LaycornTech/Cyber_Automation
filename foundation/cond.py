
name = input("Enter name: ")

while name == "":
    name = input("enter a name: ")

print(f"Hello, {name}!")


def print_hello():
    print(f"Hello, {name * 2}!")

print_hello()

def sum():
    x = 10
    y = 20
    print(x + y)
    print_hello()


sum()


