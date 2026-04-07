# Section 1 - Your code
Name = input("What is your name")
background = input("Beach or Ski")
from utils import *
set_background(f"{background}")

s1 = create_sprite("alien", 10, 100)
s2 = create_sprite("bald_eagle", -100, 100)
s2 = create_sprite("The_goat", -100, -90)
s2 = create_sprite("cardinal", 100, -90)

message1 = create_sprite("alien",-200,-200)
message1.color("green")
message1.write(f"Hi {Name} nice to meet you",font = ("Arial", 25, "normal"))
message1.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()