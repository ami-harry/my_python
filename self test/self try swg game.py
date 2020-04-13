# make a puthon game. just take input from user and start the game
# snake will drink the water
# gun will be sink into water
# snake will be shot by gun
# using these cases make the program
# and add 1 point for win and 0 for tie
# lastly print the total of yours and computers
############################################################################################

import random

options=['s','w','g']
choice=int(input("how many time do you want to try\n"))
total_no_of_choice=0
compt_pt=0
your_pt=0

print("\t\t\tWelcome to Snake-Water-Gun game\n\n")
print("Choose your guess\n 's' for Snake\n'g' for Gun\n'w' for water\n")

#makking program with while loop
while choice>total_no_of_choice:
    _input=input("Enter your choice\n'snake', 'water','gun'\n")
    _random=random.choice(options)

    # when both choose the same option
    if _input==_random:
        print("Tie, both got 0 points\n")
        print(f"computer point is {compt_pt} and your point is {your_pt}")


    #if user inputs s'
    if _input=="s" and _random=="g":
        compt_pt+=1
        print(f"computer choice is {_random} and your choice is {_input}")
        print("Computer got 1 point\n")
        print(f"computer point is {compt_pt} and your point is {your_pt}\n")

    elif _input=="s" and _random=="w":
        your_pt+=1
        print(f"computer choice is {_random} and your choice is {_input}")
        print("you got 1 point\n")
        print(f"computer point is {compt_pt} and your point is {your_pt}\n")

    #if user inputs w
    elif _input=="w" and _random=="s":
        compt_pt += 1
        print(f"computer choice is {_random} and your choice is {_input}")
        print("Computer got 1 point\n")
        print(f"computer point is {compt_pt} and your point is {your_pt}\n")

    elif _input=="w" and _random=="g":
        your_pt += 1
        print(f"computer choice is {_random} and your choice is {_input}")
        print("you got 1 point\n")
        print(f"computer point is {compt_pt} and your point is {your_pt}\n")
    # if user input g
    elif _input=="g" and _random=="w":
        compt_pt += 1
        print(f"computer choice is {_random} and your choice is {_input}")
        print("Computer got 1 point\n")
        print(f"computer point is {compt_pt} and your point is {your_pt}\n")

    elif _input=="g" and _random=="s":
        your_pt += 1
        print(f"computer choice is {_random} and your choice is {_input}")
        print("you got 1 point\n")
        print(f"computer point is {compt_pt} and your point is {your_pt}\n")

    else:
        print("enter  a valid input\n")

    total_no_of_choice= total_no_of_choice+1
    print(f"{choice-total_no_of_choice} chance is left out of {choice}\n\n")

print("game over\n")

if compt_pt<your_pt:
    print("you won\n")
elif compt_pt>your_pt:
    print("computer wins\n")
else:
    print("score level\n")
print("thanks for palying this game\n\t\t\t\tHaRrY")


