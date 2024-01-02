color = str(input("select a color from [blue,black,green]:"))
color_num = 0
if color == "blue":
    color_num = 1
elif color == "black":
    color_num = 2
elif color == "green":
    color_num = 3
else:
    print("Enter a valid color or check the spelling of the color")
for i in range(color_num,525,3):
    print(i)