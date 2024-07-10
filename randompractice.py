# rock paper scissor

x =input("enter r for rock, p for paper or else s for scissor : ")
if x == "r":
    print("you = rock")
elif x == "p":
    print("you = paper")
elif x == "s":
    print("you = scissor")
else:
    print("invalid output")
    exit()


import random
choices_values = ["r", "p", "s"]
y = random.choice(choices_values)
if y == "r":
    print("me = rock")
elif y == "p":
    print("me = paper")
elif y == "s":
    print("me = scissor")

if(x == "r" and y == "s") or (x == "p" and y == "r") or (x == "s" and y == "p"):
    print("you win")
elif(x == "r" and y == "p") or (x == "p" and y == "s") or (x == "s" and y == "r"):
    print("you loose")
else:
    print("draw")
    exit()

print("thank you")



