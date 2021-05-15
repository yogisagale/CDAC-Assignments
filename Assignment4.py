

#Q1: Write a python program to add all the odd numbers from 0 to 20.##########
list1=[]
for i in range(21):
    if i%2!=0:
        list1.append(i)
print("List of odd numbers:",list1)
sum_odd=sum(list1)
print("Sum of odd numbers:",sum_odd)

### using lambda function ###
import functools
odd_number=[x for x in filter(lambda x:x%2!=0,range(1,21))]
sum_odd=functools.reduce(lambda a,b:a+b,odd_number)
print("List of odd number:",odd_number)
print("Sum of odd number from 0 to 20 is ",sum_odd)


#Q2: Write a python program to add all the even numbers between 0 to 20.#######

total=0
list2=[]
for j in range(21):
    if j%2==0:
        list2.append(j)
        total=total+j
print("List of even number is:",list2)
print("Sum of all even numbers upto 20 is :",total)

### using lambda function ###

import functools
even_number=[x for x in filter(lambda x:x%2==0,range(1,21))]
sum_even=functools.reduce(lambda a,b:a+b,even_number)
print("List of even number:",even_number)
print("Sum of even number from 0 to 20 is ",sum_even)



#Q3: Write a python program to find the sum of all integers greater than 100 and less than 200.
total=0
for j in range(101,200,1):
        total=total+j
print("Sum of all even numbers upto 20 is :",total)   

#using sum function
total=sum(range(101,200,1))
print("sum of all integers greater than 100 and less than 200:",total)   

### using lambda
import functools
total=functools.reduce(lambda x,y:x+y,range(101,200,1))
print("sum of all integers greater than 100 and less than 200:",total) 




#Q4: Write a python program to display a Multiplication table of a number enter from keyboard.

num=int(input("Enter a number:"))
print("Multiplication table is:\n")
for i in range(1,11,1):
    print("%d * %d=%d"%(num,i,num*i))
    
    
#Q5: Write a program to display the sum of square of the first ten even natural numbers
total=0
for j in range(11):
    k=(2*j)**2
    total=total+k
print("Sum of square of first ten natuaral number is :",total) 


##lambda function##

import functools
even_square=[(2*x)**2 for x in range(1,11)]
sum_even_square=functools.reduce(lambda a,b:(a+b),even_square) 
print("Sum of squre of ten even number:",sum_even_square)
 

#Q6: Write a program to display the sum of cube of first ten even natural numbers
total=0
for j in range(21):
    if j%2==0:
        k=j*j*j
        total=total+k
print("Sum of cube of first ten even number is :",total) 

## lambda function##

import functools
even_number=[2*x for x in range(1,11) ]
even_cube=list(map(lambda y:y*y*y,even_number))
sum_cube=functools.reduce(lambda a,b:a+b,even_cube)
print("Sum of cube of first ten even number is :",sum_cube) 


#Q7: Display the sum of: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 + 1/19 + 1/22 + 1/25

i=1
j=1
total=0
while j<=25:
    k=i/j
    total=total+k
    j=j+3
print(round(total,2))

##using lambda##

import functools
d=[x for x in range(1,26,3)]
n=list(map(lambda a:(1/a),d))
sum1=round(functools.reduce(lambda a,b:a+b,n),2)
print("Sum of the expression:",sum1)



#Q8: Write a python program to display ascii characters from 65 to 90  #########

for i in range(65,91):
    print("ASCII character %d is %c"%(i,i))
    

#Q9: Display ascii characters from 48 to 57.##################################

for i in range(48,58):
    print("ASCII character %d is %c"%(i,i))

#Q10: Display the following output with the help of Ascii character.##########






#Q11: write a python program to swap two variables provided by the user.######
x=int(input("Enter value of x:"))
y=int(input("Enter value of y:"))
temp=x
x=y
y=temp

print("The value of x after swapping:",x)
print("The value of y after swapping:",y)


#Q12: The marks obtained by a student in 5 different Subjects are input through a keyboard. The Student
#gets a division as per the following rules.
#1. Percentage above or equal to 60 – First Division
#2. Percentage between 50 and 59 – Second Division
#3. Percentage between 40 and 49 – Third Division
#4. Percentage less than 40 – Fail

import functools
marks=[x for x in (map(int,input("Enter the marks of five subjects:").split(" ")))]
full=int(input("Enter the full marks of each subject:"))

if len(marks)==5:
    avg=round((functools.reduce(lambda x,y:x+y,marks))/len(marks),2)
    per=round((avg*100/full),2)
    print("Percentage of marks:",per)
    if per>=60:
        print("First Division")
    elif (per>=50 and per<=59):
        print("Second Division")
    elif (per>=40 and per<=49):
        print("Third Division")
    else:
        print("Fail")
else:
    print("Enter exactly five marks")
    
    
#Q13: write a Python program to find the largest number among the three input numbers
    
a,b,c=map(int,input("Enter three number:").split(" "))
if a>b and a>c:
    print("Largest is:",a)
elif b>a and b>c:
    print("Largest is:",b)
else:
    print("Largest is:",c)

#Q14: write a Python program to find the factorial of a number provided by the user

import functools
num=int(input("Enter the number:"))
fact=functools.reduce(lambda a,b:a*b,range(1,num+1))
print("Facorial of %d is= %d"%(num,fact))
        

#Q15: write a Python program to check if the input number is prime or not.

num=int(input("Enter a number:"))
if num>1:
    for i in range(2,num//2):
        if (num%i)==0:
            print("Entered number is not prime")
            break
    else:
        print("Entered number is a prime")
else:
    print("Enter number is not a prime")
    
    
#Q16. With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such
#that is an integral number between 1 and n (both included). and then the program should print the
#dictionary.
    
num=int(input("Enter a number:"))
dict1={x:x**2 for x in range(1,(num+1))}
print(dict1)



#Q17. Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The
#element value in the i-th row and j-th column of the array should be i*j.







#Q18. Write a program that accepts a sequence of whitespace separated words as input and prints the
#words after removing all duplicate words and sorting them alphanumerically.

sen=input("Enter a sentence:").split()
a=[]
for i in sen:
    if i not in a:
        a.append(i)
print(" ".join(sorted(a)))
        

        
        
        
    

#Q19. Use a list comprehension to square each odd number in a list. The list is input by a sequence of
#comma-separated numbers.  

list1=list(map(int,input("Enter the list of number:").split()))
list2=[x for x in list1 if x%2!=0]
list3=list(map(lambda a:a**2,list2))
print("List of odd number:",list2)
print("List of square of odd number:",list3)  
 




#Q20. Write a program to compute the frequency of the words from the input. The output should output
#after sorting the key alphanumerically.





#Q21. Define a function that can accept two strings as input and print the string with maximum length in
#console. If two strings have the same length, then the function should print al l strings line by line.

def len_stng(a,b):
    if len(a)>len(b):
        print(a)
    elif len(a)==len(b):
        print("Both strings are same length")
        print(a)
        print(b)
    else:
        print(b)
str1=input("Enter the First string:")
str2=input("Enter the second string:")
print("Largest string is:")
len_stng(str1,str2)





#Q22. Write a program to generate and print another tuple whose values are even numbers in the given
#tuple (1,2,3,4,5,6,7,8,9,10).

tup=(1,2,3,4,5,6,7,8,9,10)
tup1=tuple(filter(lambda a:(a%2==0),tup))
print("Tuple of even numbers:",tup1)

#Q23. Write a program which can filter even numbers in a list by using filter function. The list is:
#[1,2,3,4,5,6,7,8,9,10].

lis=[1,2,3,4,5,6,7,8,9,10]
list1=list(filter(lambda x:(x%2==0),lis))
print("List of even numbers:",list1)

#Q24. Write a program which can map() to make a list whose elements are square of elements in
#[1,2,3,4,5,6,7,8,9,10].

list1=[1,2,3,4,5,6,7,8,9,10]
list2=list(map(lambda x:x**2,list1))
print("List of square of given list")
print(list2)

#Q25. Write a program which can map() and filter() to make a list whose elements are square of even
#number in [1,2,3,4,5,6,7,8,9,10].


lis=[1,2,3,4,5,6,7,8,9,10]
list1=list(filter(lambda x:(x%2==0),lis))
list2=list(map(lambda x:x**2,list1)) 
print("List of square of even numbers of given list:") 
print(list2)

#Q26. Write a program which can filter() to make a list whose elements are even number between 1 and
#20 (both included).

list1=list(filter(lambda a:(a%2==0),range(1,21)))
list2=list(filter(lambda b:(b%2!=0),range(1,21)))
print("List of even numbers:",list1)
print("List of odd numbers:",list2)

