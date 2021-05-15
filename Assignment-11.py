                                                   # Assignment 11

#Q.1. Write a program that asks the user how many days are in a particular month, and what day of the
#week the month begins on (0 for Monday, 1 for Tuesday, etc), and then prints a calendar for that month.
#For example, here is the output for a 30-day month that begins on day 4 (Thursday):
#S M T W T F S
 #1 2 3
#4 5 6 7 8 9 10
#11 12 13 14 15 16 17
#18 19 20 21 22 23 24 \
#25 26 27 28 29 30
def calendar(n,day):
         l=['']*(n+day)
         for i in range(0,n):
                l[(i+day)]=i+1
         print('\n{:>3}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}'.format('Su','Mo','Tu','We','Th','Fr','Sa'),end=" ")
         for j in range(0,n+day):
              if(j%7==0):
                       print("\n")
                       print('{:3}'.format(l[j]),end=" ")
              else:
                        print('{:3}'.format(l[j]),end=" ")
day=int(input("Starting day (Sun is 0, Sat is 6) : "))
n=int(input("Number of days in the month : "))       
calendar(n,day) 

#Q. 2. Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. For
#example, histogram([4, 9, 7]) should print the following:
#****
#*********
#*******

def histogram(l):
    for i in l:
        for j in range (i):
            print("*",end="")
        print()
        
list1=list(map(int,input("Enter a comma separated list : ").split(",")))
histogram(list1)

#Q. 3. Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go hang a
#salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa
#Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori",
#"Rise to vote sir", or the exclamation "Dammit, I'm mad!". Note that punctuation, capitalization, and
#spacing are usually ignored

import re
stin=input("Enter a sentence : ")
result=re.sub(r"[^\w]*","",stin) #only alphanumeric words are allowed
result=result.upper()
if("".join(reversed(result)) == result):
    print("".join(reversed(stin)),' is a palindrome.')
else:
    print("The phrase entered is not a palindrome.")


#Q. 4. A pangram is a sentence that contains all the letters of the English alphabet at least once, for example: The quick brown fox jumps over the lazy dog. Your task here is to write a function to check a sentence to see if it is a pangram or not.
import re
l1=[]
s=set()
regex=r"[A-Za-z]{26}"
def Pangram(string):
    l1.extend(string)
    s=set(l1)
    st1=str(s)
    st1=re.sub(r"[0-9,/\'\s{}]","",st1)
    return st1
np=input("Enter a string : ")
rawstring=Pangram(np)   
if re.match(regex,rawstring):
    print("Is a Panagram : True")
else:
    print("Is a Panagram : False")

#Q4. 
class ROT13:    
    def encode(self,string):
        li=[]
        lr=''
        li.extend(string)
        for i in range(len(li)):
            #lr.append(chr(ord(li[i])-13))
            lr=lr+(chr(ord(li[i])+13))
        print("Encoded message is {}".format(lr))
    def decode(self,string):
        li=[]
        lr=''
        li.extend(string)
        for i in range(len(li)):
            #lr.append(chr(ord(li[i])-13))
            lr=lr+(chr(ord(li[i])-13))
        print("Decoded message is {}".format(lr))
    
 
ob=ROT13()
stin=input("Enter the string and encode,decode :\nFor example <abc,e> to encode\n")
sq=stin.split(',')
msg=sq[0]
op=sq[1]

if op=='e':
    res=ob.encode(msg)
elif op=='d':
    res=ob.decode(msg)
    
    

#Q.5.

people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}
print(people)
print(len(people.keys())) 
people['Lisa']='Green'    
print(people)
people.pop('Jenny')  
print(sorted(people))

for i in sorted (people) :
    print ((i, people[i])) 
    
    
#Q. 6. Write a program that contains a function that has one parameter, n, representing an integer greater
##than 0. The function should return n! (n factorial). Then write a main function that calls this function with
#the values 1 through 20, one at a time, printing the returned results. This is what your output should look
#like:
#1 1
#2 2
#3 6
#4 24
#5 120
#6 720
#7 5040
#8 40320
#9 362880
#10 3628800
    
import math
def factorial(s,e):
    for i in range(s,e):
               print("{} {}".format(i,math.factorial(i)))
def main():
    factorial(1,21)    
if __name__=='__main__':
    main()


#Q. 7.
def sum(x):
    if (x==1):
        return 1
    else:
        return(x+sum(x-1))
   
num=int(input('enter the number:'))
print("sum of the natural number upto %d is:%d"%(num,sum(num)))    

    





#Q. 8. Define a function overlapping() that takes two lists and returns True if they have at least one
#member in common, False otherwise.
def overlapping(l1,l2):
    s1= set(l1)
    s2= set(l2)
    if len(set.intersection(s1,s2))!=0:
        print("True")
    else:
        print("False")
        
l1=[1,2,3,4,5,6]
l2=[1,8,9,0,5]
overlapping(l1,l2)


#Write a function find_longest_word() that takes a list of words and returns the length of the longest
#one.
def find_longest_word(enter):
          """To find the longest word out of a list of words."""
          l=sorted(enter,key=len,reverse=True)
          print("'{}' is the longest word with length {}".format(l[0],len(l[0])))

#Q. 9.Write a function filter_long_words() that takes a list of words and an integer n and returns the list of
#words that are longer than n

enter=list(map(str,input("Enter words in the list: ").split()))
find_longest_word(enter)



#Q. 10.
def correction(stin):
    stin=re.sub(r'[\s]+'," ",stin)
    stin=re.sub(r'(\w)([\.,!]+)(\w)',r'\1\2 \3',stin)
    print(stin)

stin="This is very funny   and    cool.    Indeed!"
correction(stin)

#Q. 11.

expt=['be','see','is','flee','knee',]
def make_ing_form(stin):
    cvc=r'([bcdfghjklmnpqrstvwxyz])([aeiou])([bcdfghjklmnpqrstvwxyz])\b'
    if stin in expt:
             stin=stin
    elif stin[-2:]=='ie':
              stin=re.sub(r'(\w)(ie)\b',r'\1ying',stin)
    elif stin[-1]=='e':
               stin=re.sub(r'(\w)(e)\b',r'\1ing',stin)
    elif(re.match(cvc,stin)):
                stin=re.sub(cvc,r'\1\2\3\3ing',stin)
    else:
                  stin=re.sub(r'\b(\w+)\b',r'\1ing',stin)
                  
    print(stin)
stin=input("Enter string : ")
make_ing_form(stin)
