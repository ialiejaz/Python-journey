fruit = str(input("write the fruit name:"))
color = str(input("what color is fruit:"))

if fruit == "apple":
    if color == "green":
        print("unripe")
    elif color == "red":
        print("ripe")
    elif color == "brown":
        print("overripe")
else:
    print("give a fruit name!")

