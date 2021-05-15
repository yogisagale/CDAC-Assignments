#Write a Python Program To Display Powers of 2 Using Anonymous Function. 
#Take number of terms from user
c=int(input('enter the input:'))
a=lambda b:b**2
print('the result of lambda function:',a(c))


#Q2: Write a Python Program to find numbers divisible by thirteen from a list using anonymous function
a = [int(x) for x in input().split()]
list(map(lambda x:x%13==0,a))

#Q3: Write a Python program to find the H.C.F of two input number

import math
x,y = [int(x) for x in input().split()]
print(math.gcd(x,y))

#Q4: Write a Python Program to find the factors of a number

num = int(input("enter number to find its factors"))
for i in range(1,num+1):
    if num%i==0:
        print(i)


#Q5: Write a Program to make a simple calculator that can add, subtract, multiply and divide using functions 

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def divide(a,b):
    return a/b

print("enter 1 for add")
print("enter 2 for subtract")
print("enter 3 for multiply")
print("enter 4 for divide")


choice = input("enter your choice as 1/2/3/4:")
x=int(input("enter the input1"))
y=int(input("enter the input1"))


if choice == '1':
    print(x,"+",y,"=", add(x,y))

elif choice == '2':
    print(x,"-",y,"=", sub(x,y))

elif choice == '3':
    print(x,"*",y,"=", multi(x,y))

elif choice == '4':
    print(x,"/",y,"=", divide(x,y))
else:
    print("Invalid input")

#Q6: Write a Python program to display the Fibonacci sequence up to n-th term using recursive functions
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

#Q7: Write a Python program to find the sum of natural numbers up to n using recursive function
def recur_sum(n):
    if n <= 1:
        return n
    else:
        return n + recur_sum(n-1)

recur_sum(7)
 
#Q8: Write a Python program to convert decimal number into binary number using recursive function 
def convertToBinary(n):
    if n > 1:
        convertToBinary(n//2)
    print(n % 2,end = '')
convertToBinary(65656)    
    
    
