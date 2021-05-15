                  #Assignment – 8 (Class and Objects)

#Q1: Write a Python class to implement pow(x, n)
class power:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def pow(self):
        print("%d power of %d=%d"%(self.y,self.x,self.x**self.y))

a=int(input("Enter the number:"))
b=int(input("Enter the power of the number:"))
p=power(a,b)
p.pow()



#Q2: Write a Python class which has two methods get_String and print_String. get_String
#accept a string from the user and print_String print the string in upper case.
class string:
    def __init__(self):
        pass
    def get_string(self,x):
        self.x=x
    def print_string(self):
        return self.x.upper()
str1=input("Enter a string:")
a=string()
a.get_string(str1)
a.print_string()

##Q3: Define a class Person and its two child classes: Male and Female. All classes have
##a method "getGender" which can print "Male" for Male class and "Female" for Female class.


class person:
    def __init__(self,gen):
        self.gen=gen
class male(person):
    def getGender(self):
        return self.gen
class female(person):
    def getGender(self):
        return self.gen
           
m=male("male")
f=female("female")
print(m.getGender())
print(f.getGender())

##Q4.Define a class Polygon with the following functions:
##__init__ method: to take the take the number of sides of a polygon and
##initialize all the sides with the value 0.
##Inputside method: to take the input values of sides from the user
##DispSide method: to display all the sides of the polygon

class polygon:
    def __init__(self,s):
        self.s=[]
    def inputside(self,side):
        return self.s.append(side)
    def dispside(self,i):
        return self.s[i]
n=int(input("Enter the number of side:"))
a=polygon(n)
print("Enter the value of sides:")
for i in range(n):
    side=int(input("Enter value of side "+str(i+1)+":"))
    a.inputside(side)
print("value of each side:")    
for j in range(n):
    print(a.dispside(j),end="  ")
    


class polygon:
    def __init__(self,no_of_side):
        self.n=no_of_side
        
    def inputside(self):
        self.sides=[float(input("Enter value of side "+str(i+1)+":")) for i in range(self.n)]
    def dispside(self):
        for i in range(self.n):
            print("side",i+1,"is",self.sides[i])
a=polygon(int(input("Enter number of sides:")))
a.inputside()
a.dispside()
    

##Q5. Define a class Triangle which inherits from Polygon (use class of Q4). This class consists of
#the following function:
#CalculateArea method: to calculate the area of the triangle    



class polygon:
    def __init__(self,no_of_side):
        self.n=no_of_side
        self.sides=[0 for i in range(no_of_side)]
        
    def inputside(self):
        self.sides=[float(input("Enter value of side "+str(i+1)+":")) for i in range(self.n)]
    def dispside(self):
        for i in range(self.n):
            print("side",i+1,"is",self.sides[i])
            
class triangle(polygon):
    def __init__(self,n):
        polygon.__init__(self,n)
        
        
    def area(self):
        
        if (self.n==3):
            a,b,c=self.sides
            if((a+b)>c and (b+c)>a and (c+a)>b):
                print("Entered polygon is a triangle")
                s=round((a+b+c)/2,2)
                a=s*((s-a)*(s-b)*(s-c))
                print("Area of the triangle is %0.2f"%a)
            else:
                print("Entered polygon is not a triangle")
        else:
            print("Entered polygon is not triangle")
            
            
a=triangle(int(input("Enter number of sides:")))
a.inputside()
a.dispside()
a.area()
    




##Q6. Define a class Person with the following member functions:
#Getdata() : to take name and age of a person as an input from the user
#Showdata(): to display name and age
#Define a class Student (this class inherits Person class), with the following functions:
#Getdata(): calls Getdata() of Person class to take input as name and age. And also takes
#an extra input from user that is Student_id.
#Showdata(): calls Showdata() of Person class and also displays Student_id
#Create the object of Student class and enter the name, age and student_id and also display
#all the information of a student.    



class person:
    def __init__(self):
        self.name=0
        self.age=0
    def getdata(self):
        self.name=input("Enter a name:")
        self.age=int(input("Enter age:"))
    def showdata(self):
        print("name:",self.name)
        print("age:",self.age)
class student(person):
    def __init__(self):
        person.__init__(self)
    def Getid(self):
        self.id=input("Enter student Id:")
    def showdata(self):
        print("name:",self.name)
        print("age:",self.age)
        print("Student Id:",self.id)
        
    
a=student()
a.getdata()
a.Getid()
a.showdata()
b=person()
b.getdata()
b.showdata()


##Q7. Define a class Employee with the following functions:
#__init__() : to initialize all the variables with appropriate default values
#Displaycount(): to count the number of objects of employee class and display the count
#Displayemp(): to display the employee details


class employee:
    count=0
    def __init__(self):
        self.name=0
        self.age=0
        self.emp_id=0
        employee.count=employee.count+1
        
    def getdata(self):
        self.name=input("Enter name:")
        self.age=int(input("Enter age:"))
        self.emp_id=int(input("Enter Id number:"))
    def dispcount():
        print("\nNumber of employee:",employee.count)
        
        
    def showdata(self):
        print()
        print("Employee name:",self.name)
        print("Employee's age:",self.age)
        print("Employee Id:",self.emp_id)
emp1=employee()
emp1.getdata()
emp2=employee()
emp2.getdata()
emp1.showdata()
emp2.showdata()
employee.dispcount()


##Q8. Create a class named 'Rectangle' with two data members 'length' and 'breadth' and two
#methods to print the area and perimeter of the rectangle respectively. Its constructor having
#parameters for length and breadth is used to initialize length and breadth of the rectangle. Let
#class 'Square' inherit the 'Rectangle' class with its constructor having a parameter for its side
#(suppose s) calling the constructor of its parent class as 'super(s,s)'. Print the area and
#perimeter of a rectangle and a square.


class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        self.area=(self.length * self.breadth)
        print("Area :",self.area)
    def perimeter(self):
        self.perimeter=2*(self.length + self.breadth)
        print("Perimeter :",self.perimeter)
class square(rectangle):
    def __init__(self,length):
        rectangle.__init__(self,length,length)
        
rec=rectangle(a,b)
a=float(input("Enter the length of rectangle:"))
b=float(input("Enter the breadth of rectangle:"))
rec.area()
rec.perimeter()

c=float(input("Enter the length of square:"))
sqr=square(c)
sqr.area()
sqr.perimeter()


##Q9. Define a class ComplexNumbers with the following functions:
#Constructor: to initialize an initial value to a complex number
#__str__(): to display complex number
#Create two objects of this class and display the result.      
        
        
class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def __str__(self):
        
        return str("%0.2f"%self.real)+("+" if self.img>=0 else "-")+str("%0.2f"%abs(self.img))+"i"
        

r1=float(input("Enter real number:"))
i1=float(input("Enter imaginary number:"))
c1=complex(r1,i1)
print("Complex number 1:",c1)


r2=float(input("Enter real number:"))
i2=float(input("Enter imaginary number:"))
c2=complex(r2,i2)
print("Complex number 2:",c2)
        
         
##Q10. In the above class create a method to overload add operator to add two complex number
#and return the sum. 

class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def __str__(self):
        
        return str("%0.2f"%self.real)+("+" if self.img>=0 else "-")+str("%0.2f"%abs(self.img))+"i"
    def __add__(self,other):
        return complex((self.real+other.real),(self.img+other.img))
        

r1=float(input("Enter real number:"))
i1=float(input("Enter imaginary number:"))
c1=complex(r1,i1)
print("Complex number 1:",c1)


r2=float(input("Enter real number:"))
i2=float(input("Enter imaginary number:"))
c2=complex(r2,i2)
print("Complex number 2:",c2) 
print("\nSum of two complex number:",c1+c2) 


