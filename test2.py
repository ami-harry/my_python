#take input as the age of a man and decide wether he/she can drive or not
print("inter your age")
age=int(input())
if age>18:
    print("you can drive")
elif age==18:
    print("can't decide")
else:
    print("you are not eligible")