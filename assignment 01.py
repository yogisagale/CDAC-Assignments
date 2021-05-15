#01)Write a Python program which accept the radius of a circle from the user and compute the area.

from math import pi
r=float(input ("enter the value radius:"))
b=pi*r**2
print("Area of the circle:%0.2f"%b)

#02)Temperature of a city in Fahrenheit degrees is input through the keyboard. Write a program to convert this temperature into Centigrade degrees. 

temp=input("enter temp of the city :")
unit=temp[-1]
t=float(temp[0:-1])
if unit=="c" or unit=="C":
    print("entered temp is Centigrade degree:")
    f=((t*9)/5)+32
    print("temperature of city in Fahrenheit degree :%0.2f"%f)
elif unit=="f" or unit=="F":
     print("entered temp is Fahrenheit degree :")
     c=((t-32)/9)*5
     print("temperature of city in Centigrade degree :%0.2f"%c) 
else:
    print('enter temperature is wrong')
     
         
#Q3: Ramesh’s basic salary is input through the keyboard. His dearness allowance is 40% of basic salary, and house rent allowance is 20% of basic salary. Write a program to calculate his gross salary. 

BSAL=float(input("Ramesh Basic salary"))
DA=BSAL*0.4
HRA=BSAL*0.2
GSAL=BSAL+DA+HRA
print("Gross salary of ramesh :%0.2f"%GSAL)


#Q4: Write a Python program which accept the user's first and last name and print them in reverse order with a space between them .
a=input("enter the first name:")
b=input(" enter the second name:")
c=(a+" "+b)[::-1]
print(c)


#05)Write a Python program to get the the volume of a sphere with radius 6.
r=float(input("enter the value of volume:"))
from math import pi
v=((4/3)*pi*r*r*r)
print("volume of the sphare:",v)


#:06) If a five-digit number is input through the keyboard, write a program to calculate the sum of its digits
a=int(input("enter the five digit number :"))
sum=0
while a>0:
    rem=a%10
    a=a//10
    sum=sum+rem
print("sum=",sum)


# 07)Write a Python program to accept a filename from the user and print the extension of that.
filename = input("Input the Filename: ").split(".")
a=list(filename)
print ("The extension of the file is : ",a[-1])

#08)Write a Python program to display the first and last colors from the following list. 
#color_list = ["Red","Green","White" ,"Black"]
color_list = ["Red","Green","White" ,"Black"]
print( "%s %s"%(color_list[0],color_list[-1]))


#Q9. Write a Python program to calculate number of days between two dates.


import datetime
date_entry1 = input('Enter a date in YYYY-MM-DD format:')
year, month, day = map(int, date_entry1.split('-'))
date1 = datetime.date(year, month, day)
print("first date:",date1)
date_entry2= input('Enter a date in YYYY-MM-DD format:')
year, month, day = map(int, date_entry2.split('-'))
date2 = datetime.date(year, month, day)
print("second date:",date2)

diff=date2-date1

print("Number of days between two days:",diff)

#Q10. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.
a=input("enter the string :")
if a[0:2]=="is" or a[0:2]=="Is" or a[0:2]=="IS" :
    print(a)
else:
    print("Is ",a)
    

    


#11)Write a Python program to test whether a passed letter is a vowel or not.

l = input("Input a letter of the alphabet: ")
v=['a', 'e', 'i', 'o', 'u','A','E','I','O','U']

if l in v:
	print("%s is a vowel." % l)
    

else:
	print("%s is a not vowel." % l) 
  