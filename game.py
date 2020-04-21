# make a puthon game. just take input from user and start the game
# snake will drink the water
# gun will be sink into water
# snake will be shot by gun
# using these cases make the program
# and add 1 point for win and 0 for tie
# lastly print the total of yours and computers
############################################################################################


import random
opt=['s','w','g']
# chances=10
chances=int(input("enter how many times you want to play\n"))
no_of_chance=0
comp_pt=0
human_pt=0

print("\t\t\t Welcome to Snake-Water-Gun game\n\n")
print("'s' for snake\n 'w' for water\n'g' for gun\n\n")


while chances>no_of_chance:
    _input=input("Snake, Water or Gun:\n")
    _random=random.choice(opt)
    if _input==_random:
        print("tie, both got 0 point\n")
        print(f"computer point is {comp_pt} and your point is {human_pt}")
    #if user inputs 's'
    elif _input=="s" and _random=="g":
        comp_pt+=1
        print(f"your guess is {_input} and computer guess is {_random}\n")
        print("computer got 1 point\n")
        print(f"computer point is {comp_pt} and your point is {human_pt}\n")
    elif _input=="s" and _random=="w":
        human_pt+=1
        print(f"your guess is {_input} and computer guess is {_random}\n")
        print("you got 1 point\n")
        print(f"computer point is {comp_pt} and your point is {human_pt}\n")
    #if user inputs g
    elif _input=="g" and _random=="s":
        human_pt+=1
        print(f"your guess is {_input} and computer guess is {_random}\n")
        print("you got 1 point\n")
        print(f"computer point is {comp_pt} and your point is {human_pt}\n")
    elif _input=="g" and _random=="w":
        comp_pt+=1
        print(f"your guess is {_input} and computer guess is {_random}\n")
        print("computer got 1 point\n")
        print(f"computer point is {comp_pt} and your point is {human_pt}\n")
    # if user input w
    elif _input=="w" and _random=="s":
        comp_pt+=1
        print(f"your guess is {_input} and computer guess is {_random}\n")
        print("computer got 1 point\n")
        print(f"computer point is {comp_pt} and your point is {human_pt}\n")
    elif _input=="w" and _random=="g":
        human_pt+=1
        print(f"your guess is {_input} and computer guess is {_random}\n")
        print("you got 1 point")
        print(f"computer point is {comp_pt} and your point is {human_pt}\n")
    else:
        print("enter a valid input\n")

    no_of_chance=no_of_chance+1
    print(f"{chances-no_of_chance} is left out of {chances}\n")
print("game over\n")

if comp_pt==human_pt:
    print("game tie\n")
elif comp_pt>human_pt:
    print("computer won\n")
else:
    print("you won!!\n")
print(f"your point is {human_pt} and computer point is {comp_pt}\m")

print("thanks for playing the game,\nHave a great day\nHaRrY")



