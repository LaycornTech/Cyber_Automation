
with open("data.txt", "w") as file:
    file.write("Hello, There")
    file.write("I am a winner")

with open("data.txt", "r") as file:
    content = file.read()
    print(content)