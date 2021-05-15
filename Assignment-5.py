
##Q1: Pattern 1

row=int(input("Enter the no of rows:"))      
num=1                                        
for i in range(0,row):                       
    num=1                                    
    for j in range(0,i+1):
        print(num,end=" ")
        num=num+1
    print("\n")
    


##Q2: Pattern 2
    
row=int(input("Enter the no of rows:"))                                             
for i in range(0,row):                       
    num=i+1                                   
    for j in range(0,i+1):
        print(num,end=" ")
        num=num-1
    print("\n")   



#Q3: Pattern 3
    
row=int(input("Enter the no of rows:"))                                              
for i in range(0,row):                                                          
    for j in range(0,i+1):
        print("*",end=" ")
    print("")
    
#Q4: Pattern 4
    

def triangle(row):
    m=(row//2)+1
    for i in range(0,m):
        for j in range(0,i+1):
            print("*",end="")
        print("\r")
    for i in range(m,0,-1):
        for j in range(0,i-1):
            print("*",end="")
        print("\r")
row=int(input("Enter the number of rows:"))
triangle(row)


#Q5: Pattern 5

def mul():
    for i in range(1,11):
        print(i,end="\t|")
        for j in range(1,11):
            
            print(i*j,end="\t")
        print("\r")
mul()

#Q6: Pattern 6


num = int(input("Enter the range:"))

for i in range(num):
    for j in range((num - i) - 1):
        print(end="  ")
    for j in range(2*i+1):
        print("*", end=" ")
    print()
    

    

    