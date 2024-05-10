# guess number

import random

try:
    min=int(input("insert minimum number of range: "))
    max=int(input("insert maximum number of range: "))
except:
    print("please insert a valid number")
    
pc=random.randint(min,max)
i=5

print("you can guess five times")
while i>0:
    try:
        x=int(input(f"enter {i} number that you guess!!! "))
        if x==pc:
            print("correct you win")
            break
        elif x>pc:
            print("enter smaller")
        else:
            print("enter bigger")
        i-=1
    except:
        print("please insert a valid number")

