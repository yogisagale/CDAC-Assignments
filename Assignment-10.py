#Exercise 1

import os
def file(line):
    return os.path.join(os.getcwd(),line)
print("Your current directory is -",os.getcwd())

os.listdir(os.getcwd())
name=input("Enter the file name with extension : ")
dic=file(name)
print(dic)




#Exericse 2



file=input("Enter the file name with extension : ")
file_object = open(file,'a')

file_object.write("Welcome to robotics time.")
file_object.close()
file_object=open(file,"r")
print(file_object.read())
file_object.close()



#Exercise 3


class Triangle:
    def __init__(self,angle1, angle2, angle3):
        self.angle1=int(angle1)
        self.angle2=int(angle2)
        self.angle3=int(angle3)
        self.number_of_sides=3
    def check_angles(self):
        if (self.angle1 + self.angle2 + self.angle3 == 180):
            return True
        else:
            return False
        
a,b,c=[int(x) for x in input().split()]        
my_triangle= Triangle(a,b,c)
print(my_triangle.number_of_sides)
print(my_triangle.check_angles())





#Exercise 4: Define a class called Songs, it will show the lyrics of a song. Its __init__() method should have two arguments:self and lyrics.lyricsis a list. Inside your class create a method called sing_me_a_song that prints each element of lyricson his own line. Define a variable:
#happy_bday = Song(["May god bless you, ",
 #                  "Have a sunshine on you,",
 #                  "Happy Birthday to you !"])
#Call the sing_me_song method on this variable.


class Songs:
    def __init__(self,lyrics):
        self.lyrics=lyrics
   
    def sing_me_a_song(self):
        for item in self.lyrics:
            print(item)
            
happy_bday= Songs(["May god bless you,", "Have a sunshine on you,", "Happy Birthday to you!"])
happy_bday.sing_me_a_song()


#Exercise 5: Define a class called Lunch.Its __init__() method should have two arguments:selfanf menu.Where menu is a string. Add a method called menu_price.It will involve a if statement:
#if "menu 1" print "Your choice:", menu, "Price 12.00", if "menu 2" print "Your choice:", menu, "Price 13.40", else print "Error in menu".
#To check if it works define: Paul=Lunch("menu 1") and call Paul.menu_price().


class Lunch:
    def __init__(self,menu):
        self.menu=menu
    def menu_price(self):
        if self.menu=="menu 1":
            print('Your choice:",menu, "Price 12.00')
        elif self.menu=="menu 2":
              print('Your choice:",menu, "Price 13.40')
        else:
            print("Error in Menu")
a=input("enter the menu:")
Paul=Lunch(a)
Paul.menu_price()





#Exercise 6: Define a Point3D class that inherits from object Inside the Point3D class, define an __init__() function that accepts self, x, y, and z, and assigns these numbers to the member variables self.x,self.y,self.z. Define a __repr__() method that returns "(%d, %d, %d)" % (self.x, self.y, self.z). This tells Python to represent this object in the following format: (x, y, z). Outside the class definition, create a variable named my_point containing a new instance of Point3D with x=1, y=2, and z=3. Finally, print my_point.class point3D(object):

class point3D:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)

a,b,c=[int(x) for x in input().split()]
my_point=point3D(a,b,c)
print (my_point)