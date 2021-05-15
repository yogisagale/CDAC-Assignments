#Q1: Write a Python program to sum all the items in a list.
#Q2:Write a Python program to get the largest number from a list.
#Q3: Write a Python program to get the smallest number from a list.

list1=list(input("enter the list: ").split(" "))
list2=[]
x=input("Enter the choice(1-sum/2-max/3-min):")


if x=="1":
    for i in list1[0:]:     
        list2.append(int(i))
        
    y=sum(list2)
    print("Sum of all elements in given list: ",y )
elif x=="2":
    print(max(list1))
elif x=="3":
    print(min(list1))
else:
    print("please try again")
    
#Q4: Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.    
    
list1=list(input("enter the list: ").split(" "))
print("list=",list1)
print("tuple=",(list1)) 

#Q5: Write a Python program to print out a set containing all the colors from a list which are not present in another list   

color_list_1 =set(input("enter the list: ").split(" "))
color_list_2 =set(input("enter the list: ").split(" "))
new_color_list=[]
for color in color_list_1:
   if color not in color_list_2:
     new_color_list.append(color)
new_color_list=set(new_color_list)     
print (new_color_list)     
        
#Q06:Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string

string=input("enter the string: ")
if len(string)>4:
    str1=string[0:2]+string[-2:]
    print(str1)
else:
    print("sorry")
    
#Q07)Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
#Sample String : 'restart'
#Expected Result : 'resta$t'
 
str1=input("enter the string:")
let1=str1[0]
str2=let1
for i in str1[1:]:
    if i==let1:
        i="$"
    str2=str2+str(i)
print(str2)
    
#08)Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
#Sample String : 'abc', 'xyz' 
#Expected Result : 'xyc abz'
str1=input("enter the 1st string:")
str2=input("enter the 2nd string:")
x=str1[:2]

y=str2[:2]

print(y+str1[2:len(str1)] +" "+ x+str2[2:len(str2)])

#09)Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string is already ends with 'ing' then add 'ly' instead.
str1=input("enter the string:")
x=str1[-3:]
if x=="ing":
    y=("ly")
    z=(str1+y)
    print(z)

else:
    y=("ing")
    z=(str1+y)
    print(z)
    
#10)Write a Python program to change a given string to a new string where the first and last chars have been exchanged.   
str1=input("enter the string:")
a=str1[:1]
z=str1[-1:]
print(z+str1[2:len(str1)]+a)

#11)Write a Python program to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2). 
str1=input("enter the string:") 
a=str1[-2:]  
b=a*4 
print(b)
    
#Q12: Write a Python program to add key to a dictionary.
#Sample Dictionary : {0: 10, 1: 20}
#Expected Result : {0: 10, 1: 20, 2: 30}
dict1={0: 10, 1: 20}
dict2={0: 10, 1: 20, 2: 30}
dict3={**dict1,**dict2}
print(dict3)








#Q13: Write a Python program to concatenate following dictionaries to create a new one.
#Sample Dictionary : 
#dic1={1:10, 2:20} 
#dic2={3:30, 4:40} 
#dic3={5:50,6:60}
#Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60}
dic4={**dic1,**dic2,**dic3}
print(dic4)