# write a program which accept input and compare with a pre-set no. give limited chance to user to guess the no. if trial limit is obver
# print his trial and if he succeed then give that in how many times did he has completed the challange

num=int(input("enter the pre-set number\n"))
no_of_try=1
ini_limit=1
limit=int(input("how many times did you want to try?\n"))
while(ini_limit <= limit):
    guess = int(input("enter your guess no\n"))
    if (guess < num):
        print("you have enterd smaller number\n")
    elif (guess > num):
        print("you have entered bigger number\n")
    else:
        print("you won!!,\n")
        print("you have taken",ini_limit,"to guess the number\n")
        break
    print(limit-ini_limit, "no of guesses left")
    ini_limit = ini_limit + 1
    if (limit<ini_limit):
        print("you lost")