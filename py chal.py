# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 00:14:26 2020

@author: yogisasagale

"""
# problem 1
str1=input("Enter the company name:")
str2=str1.replace(" ","")
if(len(str2)>=3):
    dict1={}
    for x in str2:
        if x in dict1.keys(): 
            dict1[x]+=1
        
        else:
            dict1[x]=1
    sortdict=sorted(sorted(dict1.items(),key=lambda t:t[0]),key=lambda t:t[1],reverse=True)
    print("First three Character and its occurence :")
    
    for i in range(3):
        print(sortdict[i])
    print("The company logo is:")
    for i in range(3):
        print(sortdict[i][0],end="")
    
else:
    print("Please Enter valid company name")


#Problem 2

f=ord("F")   #ascii value of F=70
e=ord("Q")   #ascii value of Q=81
for i in range(f,e):
    print(i,end=" ")



#Problem 3



dna="ATGC"
nuclecide=input("Enter DNA nuclecide:")
rna=""
for i in nuclecide:
    if i not in dna:
        print("Invalid nuclecide.")
        break
    elif(i=="G"):
        rna+="C"
    elif(i=="C"):
        rna+="G"
    elif(i=="T"):
        rna+="A"
    else:
        rna+="U"
print("RNA nuclecides are:",rna)


#Problem 4


l=ord("\n")  #ASCII value of \n =10
e=ord("*")   #ASCII value of *=42
n=l*e        #42*10=420
print(n)



#Problem 5
    
a,b,c=map(int,input("Enter three number:").split(" "))
a,b=b,a
a=a*c
b=b+c
print("The output is:%d %d"%(a,b))



