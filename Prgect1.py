print("The only rules are dont press space before answering and chose one of the options on screen if given")
input()
name=input("Hi what is you name")
print(f"Hi {name} how is your day")
input()
print("nice so what is your favorite color?")
input()
answer1 = input("me too, do you think im a line of code and every time you you say something I just go to the next automated answer yes or no")
if answer1 == "yes":
    answer2 = input("Im not and if you want proof I answered your question and if you said something different I would have said something different")
if answer1 == "no":
    answer3 = input("Im glad you have faith in me")
print("want to play a game")
input()
print("lucky you you get to")
input()
print("pick a number between 1-2 but dont type it")
input()
print("I bet it was 1 or 2 cool right i just guessed " \
"the number")
input()
answer1 = input("alright new game If 1+2=4 what dose 2+2= type your answer")
if answer1 == "67":
    answer2 = input("Wow you must have cheated or something good job")
else:
    answer3 = input("wrong try again")
    if answer3 == "67":
        print("Wow you must have cheated or something good job")
    else:
        print("No not close but I will give it to you the answer was 67")
input()
print(fr"thanks for talking to me {name} :)")