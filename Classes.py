#This is a class
#We use clases to define new types, this types have metodes that
#we define in the body of the class
#And they can also have attributes that we can set anywhere in our program
class Point:
    def move(self):
        print("move")
    def draw(self):
        print("draw")


#This is an object with attributes
point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()
#This is another object with attributes
point2 = Point()
point2.x = 1
point2.y = 2
print(point2.y)