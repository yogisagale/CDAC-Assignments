# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 09:52:20 2020

@author: Yog
"""

# Q1. write a Python program to check if the input year is a leap year or not.

year=int(input('Enter Year:'))
if (year%4==0):
	if(year%100==0):
         if(year%400==0):
        	 print("This  is leap  year")
         else:
             print("This is not leap year")
             
	else:
    	 print("This is leap year")
else:
	leap=False
print("This is not leap year")

#02)write a Program to display the Fibonacci sequence up to n-th term where n is provided by the user

num=int(input("Enter a number: "))
def fibonacci(n):
	a=0
	b=1
	for i in range(n):
         yield a
         a,b=b,a+b
for x in fibonacci(num):
	print("\n fibonacci series: ",x,end=' ')
    
#Q3. write a Program to check if a string is palindrome or not

str1=input("Enter a string: ")
if str1=="".join(reversed(str1)):
	print(str1, "is a palindrome.")
else:
	print(str1,"is not a palindrome!")
    
    
    
#04)write a Program to sort alphabetically the words form a string provided by the user. [You can use split() method to split string into a list of words. ]
list1=input("enter the string: ").split()
list1.sort()
print(" ".join(list1))




# #Q5. write a Program to Remove Punctuations from a String provided by the user
import re
p=re.compile('[a-z]+', flags=re.IGNORECASE)
str1=input("Enter your string: ")
result_str=p.findall(str1)
print(list(result_str))


#Q6. Write a Python program to find sequences of lowercase letters joined with a underscore.  
import re
p=re.compile('[a-z]+_[a-z]+')
str1=input("Enter string:")
result_str=p.findall(str1)
print(list(result_str))

#Q7. Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re
p=re.compile('[A-Z]{1}[a-z]+')
str1=input("Enter string:")
result_str=p.findall(str1)
print(list(result_str))


#Q8. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re
p=re.compile(r'\ba\w*?b\b',flags=re.IGNORECASE)
str1=input("Enter string:")
result_str=p.findall(str1)
print(list(result_str))


#Q9. Write a Python program that matches a word containing 'z', not at the start or end of the word.
import re
p=re.compile('\w+z+\w+',flags=re.IGNORECASE)
str1=input("Enter string:")
result_str=p.findall(str1)
print(list(result_str))



#Q10. Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.
import re
p=re.compile('\w+',flags=re.IGNORECASE)
str1=input("Enter string:")
result_str=p.findall(str1)
print(list(result_str))

#Q11. Write a Python program where a string will start with a specific number.
import re
p=re.compile('^\d+\w+',flags=re.IGNORECASE)
str1=input("Enter string:")
result_str=p.findall(str1)
print(list(result_str))

#Q12. Write a Python program to remove leading zeros from an IP address.
import re
str1=input("Enter your IP address: ")
p=re.sub(r'\b0+(\d+)',r'\1',str1)
print(p)

#Q13. Write a Python program to check for a number at the end of a string.
import re
p=re.compile('\w+[0-9]+', flags=re.IGNORECASE)
str1=input("Enter your string: ")
result_str=p.findall(str1)
print(list(result_str))

#Q14. Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string.
import re
p=re.compile(r'[0-9]{1,3}')
str1=input("Enter string:")
result_str=p.findall(str1)
print(list(result_str))


#Q15. Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs.

#Q16. Write a Python program to find the substrings within a string. 
#Sample text : 'Python exercises, MachineLearning exercises, NLP exercises'
#Pattern : 'exercises'
#string='Python exercises, MachineLearning exercises, NLP exercises'
#substring='exercises'
#if substring in string:
#	print(substring)
#    2=>               
import re
p=re.compile(r'\bexercises\b')
str1=input("Enter string:")
result=p.findall(str1)
print(set(result))
#Q18. Write a Python program to extract year, month and date from an string.
def findMonthAndDate(string):
	regex=r"(\d{4}) ([a-zA-Z]+) (\d{1,2})"
	match=re.search(regex, string)
	if match==None:
    	 print("Not a valid date")
    	 return
	print("Given Data: %s " %(match.group()))
	print("Year: %s" %(match.group(1)))
	print("Month: %s" %(match.group(2)))
	print("Day: %s" % (match.group(3)))
findMonthAndDate('2000 Jun 4')
print(' ')
findMonthAndDate(' I was born on 2000 Jun 14')

#Q19. Write a Python program to find all words starting with 'a' or 'e' in a given string. 


#Q20. Write a Python program to abbreviate 'Road' as 'Rd.' in a given string.

str1=input("Enter string:")
result=str1[0]+str1[-1]
print(result)





    