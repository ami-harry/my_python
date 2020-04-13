# wap a program and set a no as default, accept input and compare every time with the default value.
# set no of guesses, if it is crossed then print game over.
# if he guess the right one print the he has entered correct input and t=took this much guesses

preset_no=int(input("enter your number\n"))
set_ini=1
limit=int(input("enter how many times did you want to try"))
while(limit >= set_ini):
    guess=int(input("enter your guess no"))
    if(guess < preset_no):
        print("you have entered smaller number")
    elif(guess > preset_no):
        print("you have entered bigger number")
    else:
        print("you won!!, your guess is right")
        print("you have completed in ",set_ini,"times")
        break
    print("you have ",limit-set_ini,"chance left")
    set_ini= set_ini+1
    if (set_ini > limit):
        print("you lost")






"""
pre_set_no = int(input("enter a pre-default value\n"))
no_of_guess = 1
print("you can try 9 times only!\n")
while(no_of_guess <= 9):
    guess_no=int(input("enter your guess no\n"))
    if guess_no < pre_set_no:
        print("you have entered smaller no, try again!")
    elif guess_no > pre_set_no:
        print("you have entered bigger no, try again!")
    else:
        print("wow!, you have guessed correct no\n you won!!!!")
        print("you took",no_of_guess,"times to guess the correct no\n")
        break
    print(9-no_of_guess,"number of guesses left:")
    no_of_guess = no_of_guess + 1
    if(no_of_guess>9):
          print("gave over")"""

