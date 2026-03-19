midfild_points = 0
defence_points = 0
atack_points = 0

print(r" ~.-~.-~.-~.-~.-~.-~.-~.-~.-~.-~.-~.-~.-~.-~.-~.-~.-~.-~.-~.-~.-~.-~.-~.-~.-~.-~.-~.-~.-")
print(r"|I can tell you what lacrosse position you would do good at just answer a some questions|")
print(r" ~.-~.-~.-~.-~.-~.-~.-~.-~.-~.-~.-~.-~.-~.-~.-~.-~.-~.-~.-~.-~.-~.-~.-~.-~.-~.-~.-~.-~.-")
input()
print("How are your stick skills")
print(" ")
print("- A emaculate")
print("- B meh")
print("- C terrible")
answer1 = input()
if answer1 == "A" or answer1 == "a": 
     atack_points += 3 
     midfild_points += 1
elif answer1 == "B" or answer1 == "b": 
     midfild_points += 1 
     defence_points += 1
elif answer1 == "C" or answer1 == "c": 
     defence_points += 3

print(r"~-~-~-~-~-~-~-~-~-~-~-~-~-~")

print("Do you like cardio")
print("")
print(" - A I love cardio")
print(" - B I dont hate It")
print(" - C I hate running")
answer2 = input()
if answer2 == "A" or answer2 == "a": 
     midfild_points += 2 
     defence_points += 1
elif answer2 == "B" or answer2 == "b":  
     defence_points += 1 
     atack_points += 1
elif answer2 == "C" or answer2 == "c": 
     atack_points += 2

print(r"~-~-~-~-~-~-~-~-~-~-~-~-~-~")

print("How fast can you pass and shoot")
print("")
print(" - A Really strong")
print(" - B Average")
print(" - C I need to get stronger")
answer3 = input()
if answer3 == "A" or answer3 == "a": 
     midfild_points += 2
elif answer3 == "B" or answer3 == "b": 
     atack_points += 1 
     defence_points += 2
elif answer3 == "C" or answer3 == "c": 
     defence_points += 3

print(r"~-~-~-~-~-~-~-~-~-~-~-~-~-~")

print("How is your shot aim")
print("")
print(" - A I can hit top right first try")
print(" - B Could be better")
print(" - C I need to practice")
answer4 = input()
if answer4 == "A" or answer4 == "a": 
     atack_points += 3 
     midfild_points += 2
elif answer4 == "B" or answer4 == "b": 
     midfild_points += 1
elif answer4 == "C" or answer4 == "c": 
     defence_points += 2

print(r"~-~-~-~-~-~-~-~-~-~-~-~-~-~")

print(" How Is your game IQ")
print("")
print(" - A I could play With my eyes closed")
print(" - B I have a good undrstanding of the game")
print(" - C I have no clue what is going on")
answer5 = input()
if answer5 == "A" or answer5 == "a": 
     atack_points += 3 
     midfild_points += 1
elif answer5 == "B" or answer5 == "b": 
     midfild_points += 1 
     defence_points += 1
elif answer5 == "C" or answer5 == "c": 
     midfild_points += 2

print(r"~-~-~-~-~-~-~-~-~-~-~-~-~-~")

print(" How Is your agility")
print("")
print(" - A I could fold a D1 long pole")
print(" - B Its respectable")
print(" - C I can barely do a split dodge")
answer6 = input()
if answer6 == "A" or answer6 == "a": 
     atack_points += 2
     midfild_points += 2 
elif answer6 == "B" or answer6 == "b": 
     defence_points += 1 
     midfild_points += 1
elif answer6 == "C" or answer6 == "c": 
     midfild_points += 1
if atack_points > defence_points and atack_points >= midfild_points: 
     print("You should play Atack")
     print(f"Your scrore was {midfild_points} midfild points {defence_points} defence points and {atack_points} atack points.")
elif midfild_points > defence_points and midfild_points >= atack_points: 
     print("You would do great at Midfield")
     print(f"Your scrore was {midfild_points} midfild points {defence_points} defence points and {atack_points} atack points.")
elif defence_points > midfild_points and defence_points >= atack_points: 
     print("You should play Defence")
     print(f"Your scrore was {midfild_points} midfild points {defence_points} defence points and {atack_points} atack points.")
elif atack_points == defence_points and atack_points == midfild_points: 
     print("You will do great at any position you please")
     print(f"Your scrore was {midfild_points} midfild points {defence_points} defence points and {atack_points} atack points.")
elif midfild_points == defence_points and midfild_points == atack_points: 
     print("You will do great at any position you please")
     print(f"Your scrore was {midfild_points} midfild points {defence_points} defence points and {atack_points} atack points.")
elif defence_points == midfild_points and defence_points == atack_points: 
     print("You will do great at any position you please")
     print(f"Your scrore was {midfild_points} midfild points {defence_points} defence points and {atack_points} atack points.")