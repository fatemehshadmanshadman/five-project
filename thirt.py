# math queztion

import random
import time

def queztion():
    action=['+','-','*','/']
    operat=random.choice(action)
    num1=random.randint(1,9)
    num2=random.randint(1,9)
    print(f"{num1} {operat} {num2} = ?")
    if operat=='+':
        return num1+num2
    elif operat=='-':
        return num1-num2
    elif operat=='*':
        return num1*num2        
    elif operat=='/':
        try:
            return num2/num1
        except ZeroDivisionError:
            return "error zero division"

point=0
q_limit=5
que=0
t_limit=5

while que<q_limit:

    result=str(queztion()) #چون مقایسه می کنیم هر دو بارد از یک جنس باشند و ممکنه کاربر کاراکتر وارد کنه
    t_start=time.time()
    answer=input("enter your answer : ")
    t_end=time.time()
    t_stop=t_end-t_start
    if t_stop<=t_limit:
        if answer==result:
            point+=1
            print(f"you good your point is{point}")
        else :
            print(f"wrong answer your point is{point}")   
        
    else:
        print("your time is finish")
        break
    que+=1

print(f"generate {que} queztions and your point is {point}")  