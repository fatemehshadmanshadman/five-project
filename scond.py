#guess character of word

from random import choice

# def printt(str:list):
#     s=""
#     for i in str:
#         s+=i
#     return s

words=["tree"]
select=choice(words)
count=len(select)

#code of video
guess=['__ ']*count
print(" ".join(guess))
while count>0:
    guess_char=input("enter guess char: ")
    if guess_char.isalpha() and len(guess_char)==1:
        if guess_char not in guess:
            if guess_char in select:
                for idx,char in enumerate(select):
                    if char==guess_char:
                        guess[idx]=guess_char
                print(" ".join(guess))
                if "__ " not in guess:
                    print("you win")
                    break
                
            else:
                count-=1
                print(f"wrong!! you have {count} chanc")
        else:
            print("you enter char beafour")
    else:
        print("enter valid and one char ")

if count==0 :
    print("you gameover")











# for i in select:
#     t+="__ "
#     temp.append("__ ")
# print(printt(temp))

# while count>0:
        
#     char=input("guess your charactor: ")
#     if char.isalpha() and len(char)==1:
#         if char not in temp:
#             indexf=select.find(char)
#             if indexf<0:
#                 print("this word not contain this char")
#                 count-=1
#             else:
#                 temp[indexf]=char
#                 indexl=select.rfind(char)
                
#                 if indexl>0 and indexf!=indexl:
#                     temp[indexl]=char
                    
                
#                 print(printt(temp)) 
#                 #if the word is complete , check this word after while

#         else:
#             print("you enter char befoure")
#     else:
#         print("enter valid char or one char")

# if select==printt(temp):
#     print("you win")
# else :
#     print("you gameover")
#     print(select)