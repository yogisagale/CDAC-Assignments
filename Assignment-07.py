#Assignment 7
#Q1. Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re
str1=input("Enter your string: ") 
print(re.sub("[ ,.]",":",str1))

# Q2. Write a Python program to replace maximum 2 occurrences of space, comma, or dot with a colon.

import re
str1=input("Enter your string: ")
print(re.sub("[( ,.){1,2}]",":",str1))

# Q3. Write a Python program to find all five characters long word in a string. 
import re 
str1=input("Enter your string: ") 
print(re.findall(r"\b\w{5}\b",str1))

# Q4. Write a Python program to find all three, four, five characters long words in a string. 
import re 
str1=input("Enter your string: ") 
print(re.findall(r"\b\w{3,5}\b",str1))

# Q5. Write a Python program to find all words which are at least 4 characters long in a string. 

import re 
str1=input("Enter your string: ") 
print(re.findall(r"\b\w{4,}\b",str1))


#Q6. Write a Python program to remove everything except alphanumeric characters from a string. 
import re 
str1=input("Enter your string: ") 
print(re.findall(r"\b\w+\b",str1)) 

#Q7. Write a Python program to split a string at uppercase letters. 

import re
str1=input("Enter your string: ")
print(re.split('[A-Z]+', str1))

# Q8. Write a Python program to check a decimal with a precision of 2. 
import re
str1=input("Enter your string: ")
print(re.findall(r'\b\d+\.\d{2}\b', str1))


# Q9. Write a python program to replace all html tags by the space in the given string. For example: Input String: “<html> This is a python regular expression. </html>” Output String: This is a python regular expression. 
import re
str1=input("Enter your string: ")
print(re.sub("<.*?>"," ",str1))


#Q10. . Write a python program to extract all the email addresses from the given string and print the output as shown below: Input String: “email address alibaba1_@google.com second email address abc_12@gmail.com” Output String: email address : alibaba1_@google.com Email id: alibaba1_ Domain: google.com Email address: abc_!2@gmail.com Email id: abc_12 Domain: gmail.com 
import re
str1=input("Enter your string: ")
p=re.compile("\b([\w\-._%+]+)@+?([\w\_]+).([A-Za-z.]+)\b") 
str2=re.split('@', str1) 
print("Email Id: ", str2[0]) 
print("Domain Name: ", str2[1])

