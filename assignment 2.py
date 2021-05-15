#	Q1: Write a Python Program to make a simple calculator that can add, subtract, multiply and divide 
a=int(input("enter the first number:"))
b=int(input("enter the first number:"))
c=input("enter the choice-+,-,*,/:")
if c=="+":
    print("addition of two number is:",a+b)
elif c=="-":
    print("substraction of two number is:",a-b)
elif c=="*":
    print("multiplication of two number is:",a*b)
elif c=="/":
    print("division of two number is:",a/b)
    
else:
    print("nothing")

   
#02)Write a Python Program to calculate the square root

import math
a=float(input("enter the number:"))
b=math.sqrt(a)
print("squre root of the given number:%0.2f"%b)

#03)Write a Python Program to Solve the quadratic equation ax**2 + bx + c = 0

import cmath

a = float(input("enter the value  a:"))
b = float(input("enter the value  b:"))
c = float(input("enter the value  c:"))


d = (b**2) - (4*a*c)


sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are '.format(sol1,sol2))

#04)Write a Python Program to find the area of triangle
# Three sides of the triangle a, b and c are provided by the user
a = float(input('Enter first side: '))  
b = float(input('Enter second side: '))  
c = float(input('Enter third side: '))  

s = (a + b + c) / 2

area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
  
print('The area of the triangle is %0.2f' %area)   


#05)Write a Python program to convert decimal number into binary, octal and hexadecimal number system
dec=int(input("Enter the decimal number:"))
choose=input("choose the conversion name: (2-Binary/8-Octal/16-Hexa-decimal): ")
x=dec
a=[]
str1=""
#from decimal to binary
if choose=='Binary' or choose=='2':
    while dec>0:
        rem=dec%2
        dec=dec//2
        a.append(rem)
    for i in a[::-1]:
        str1=str1+str(i)
    print("Binary number of %d is %s"%(x,str1))
    
# from decimal to octal
    
elif choose=='Octal' or choose=='8':
    
     while dec>0:
        rem=dec%8
        dec=dec//8
        a.append(rem)
     for i in a[::-1]:
        str1=str1+str(i)
     print("Octal number of %d is %s"%(x,str1))
     
# from decimal to Hexa-decimal
     
elif choose=='Hexa-decimal' or choose=='16':
    
     while dec>0:
        rem=dec%16
        dec=dec//16
        if rem<10:
            rem=rem
        elif rem==10:
            rem='A'
        elif rem==11:
            rem='B'
        elif rem==12:
            rem='C'
        elif rem==13:
            rem='D'
        elif rem==14:
            rem='E'
        else:
            rem='F'
        
        a.append(rem)
     for i in a[::-1]:
        str1=str1+str(i)
     print("Hexa-decimal number of %d is %s"%(x,str1))
        



#06)Write a python Program to convert kilometers into miles 
print("Enter 1 for Mile to KM")   
print("Enter 2 for KM to Mile")  
x=input("Enter the choice:")
if x=="1":
    a=float(input("enter the mile value:"))
    b=a*1.6
    print("The km value is:%0.2f"%b)
elif x=="2":
    c=float(input("enter the distance in km:"))
    b=c/1.6
    print("enter the mile value:%0.2f"%b)
else:
    print("sorry")


#07)Write a Python program to check whether a specified value is contained in a group of values.
#Test Data:
#3 -> [1, 5, 8, 3] : True
#-1 -> [1, 5, 8, 3] : False
list1=list(input("enter the list: ").split(" "))
print("list of number:",list1)
ch=input("enter the checking object: ")
print(ch in list1)




#08)Write a Python program to concatenate all elements in a list into a string and return it.
list1=list(input("enter the list: ").split(" "))
print(list1)
str1=""
for i in list1[0:]:
    str1=str1+str(i)
print("converted list into string:",str1)


#09) Write a Python program to get the least common multiple (LCM) of two positive integers.

a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
if a>b :
        max=a
        min=b
else:
    max=b
    min=a
while(1):
    if(max%a==0 and max%b==0):
        print("lcm of two number:",max)
        break
    max=max+1

#.10) Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).



import math
a,b=[int(x)for x in input("enter x1,y1 value:").split()]
print(a,b)
c,d=[int(x)for x in input("enter x2,y2 value:").split()]
p1=[a,b]
p2=[c,d]
type(p1)
distance=math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))
print(distance)


