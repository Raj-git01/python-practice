name = input("What's your name: ")
with open("name.txt" , "w") as file:
    file.write(name)
