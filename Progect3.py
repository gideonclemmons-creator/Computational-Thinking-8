from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 = -200
y1 =200
x2 =-200
y2 =100
x3 =-200
y3 =0
x4 =-200
y4 =-100
x5 =-250
y5 =-250

# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("beach")
t1 = create_sprite("balloon",x1,y1)
t2 = create_sprite("lebron(1)",x2,y2)
t3 = create_sprite("corgi",x3,y3)
t4 = create_sprite("Tia",x4,y4)
t5 = create_sprite("alien",x5,y5)

# # Section 3 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - explain here which sprites are faster or slower z1 is slow always lose x2 most likely win 8 wil ether be second or third and x3 usualy win if not x4 will
for i in range(35):
     x1 += 5
     x2 += 12
     x3 += 8
     x4 += random.randint(1,15)

     t1.goto(x1, y1)
     t2.goto(x2, y2)
     t3.goto(x3, y3)
     t4.goto(x4, y4)

     window.update()
     time.sleep(0.1)


# # Section 4 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
# s5 = create_sprite("alien",-200,-200)
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    t5.write("Player 1 wins!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
    t5.write("player 2 wins!")
elif x3 >= x1 and x3 >= x2 and x3 >= x4:
     t5.write("player 3 wins!")
elif x4 >= x1 and x4 >= x2 and x4 >= x3:
     t5.write("player 4 wins!")

turtle.exitonclick()