# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 22:17:06 2020

@author: Yogesh
"""


##1. Use a list comprehension to square each odd number in a list. The list is input by a sequence of
#comma-separated numbers.


list1=list(map(int,input("Enter numbers:").split(",")))
list2=list(x for x in list1 if x%2!=0)
list3=list(map(lambda x:x**2,list2))
print(list3)


##2. Write a program that computes the net amount of a bank account based a transaction log from
##console input. D means deposit while W means withdrawal.



def trans():
    trans_count=0
    trans=str()
    total=0
    while(1):
        trans=input("Enter the transaction (D/W):")
        if(trans=="T"):
            print("Transaction complete")
            break
        else:
            
            type_trans=trans[0]
            val_trans=int(trans[1:].strip())
            if(type_trans=="D" or type_trans=="d"):
                total=total+val_trans
                trans_count=trans_count+1
            elif(type_trans=="W" or type_trans=="w"):
                if(total<val_trans):
                    print("You can not withdrawal due to low balance")
                else:
                    total=total-val_trans
                    trans_count=trans_count+1
            else:
                print("Invalid transaction")
    print("Total number of transaction:",(trans_count))
    print("Current balance :",total)
trans()


##3. A website requires the users to input username and password to register. Write a program to
#check the validity of password input by users.
#Following are the criteria for checking the password:
#1. At least 1 letter between [a-z]
#2. At least 1 number between [0-9]
#3. At least 1 letter between [A-Z]
#4. At least 1 character from [$#@]
#5. Minimum length of transaction password: 6
#6. Maximum length of transaction password: 12

import re
list1=["ABd1234@1","a F1#","2w3E*","2We3345"]
list2=[w for w in list1 if re.search(r'[[A-Z]{1,}[a-z]{1,}[0-9]{1,}[@#$]{1,}]{6,12}',w)]
print(list2)


import re
list1=list(input("Enter the password list:").split(","))
list2=[]
for i in list1:
    if(len(i)<6 or len(i)>12):
        pass
    
    elif not re.search("[a-z]",i):
        pass
    elif not re.search("[0-9]",i):
        pass
    elif not re.search("[A-Z]",i):
        pass
    elif not re.search("[$#@]",i):
        pass
    elif re.search("\s",i):
        pass
    else:
        list2.append(i)
print(list2)
       
                    

                    
##4. A robot moves in a plane starting from the original point (0,0). The robot can move toward UP,
#DOWN, LEFT and RIGHT


x=0
y=0
def move():
    global x
    global y
    move=""
    print("Initial point is:(%d,%d)"%(x,y))
    while(1):
        move=input("Enter the movement(UP/DOWN/LEFT/RIGHT):")
        if(move=="END"):
            print("Movement completed")
            break
            
        else:
            m=move.split()
            side_move=m[0]
            val_move=int(m[1])
            if(side_move=="UP"):
                y=y+val_move
            elif(side_move=="DOWN"):
                y=y-val_move
            elif(side_move=="LEFT"):
                x=x-val_move
            elif(side_move=="RIGHT"):
                x=x+val_move
            else:
                print("Invalid movement")
            
        
    print("Current position:(%d,%d)"%(x,y))

def dist():
    global x
    global y
    dist=(x**2 + y**2)**0.5
    print("Distance from the origin %0.2f"%dist)
move()
dist()