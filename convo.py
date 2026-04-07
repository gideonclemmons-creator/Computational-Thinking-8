# Section 1 - Your code
from utils import *
player_name = input("What is your name?    ")

set_background("saas")

s1 = create_sprite("Alex", -200, -50)
s2 = create_sprite("Tia", 200, -50)
s3 = create_sprite("Tia", 100, 20)
s3.hideturtle()

s1.color("Black")
s3.color("grey")
time.sleep(2)

s1.write("Where are we?",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s1.clear()
window.update()
time.sleep(1)

s3.write("At saas!",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s3.clear()
window.update()
time.sleep(1)

s1.write(f"I'm looking for {player_name}",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s1.clear()
s1.write(f"Have you seen {player_name} ?",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s1.clear()
window.update()
time.sleep(1)

s3.write("No!",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s3.clear()
window.update()
time.sleep(1)

s3.write("Do you know were to find a dounut!",font = ("Arial", 12, "normal"))
window.update()
time.sleep(1)

s3.clear()
window.update()
time.sleep(1)

s1.clear()
s1.write(f"Yeah ?",font = ("Arial", 12, "normal"))
window.update()
time.sleep(1)

s1.clear()
window.update()
time.sleep(1)

s1.clear()
s1.write(f"There is this realy good place ",font = ("Arial", 12, "normal"))
window.update()
time.sleep(1)

s1.clear()
window.update()
time.sleep(1)

s1.clear()
s1.write(f"Down the street ",font = ("Arial", 12, "normal"))
window.update()
time.sleep(1)

s1.clear()
window.update()
time.sleep(1)

s1.clear()
s1.write(f"I order like 20 and they charge me like $10",font = ("Arial", 12, "normal"))
window.update()
time.sleep(1)

s1.clear()
window.update()
time.sleep(1)
######################################################################
# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()