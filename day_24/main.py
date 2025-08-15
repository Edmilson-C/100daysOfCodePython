with open("file.txt", mode="w") as file:
    file.write("A text written using python code")

with open("file.txt") as file:
    contents = file.read()
    print(contents)