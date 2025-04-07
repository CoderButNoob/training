import math

class Shape :

    def area(self):
        pass 

    def perimenter(self):
        pass 

class Circle(Shape):

    def __init__(self , radius):
        self.radius  = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimenter(self):
        return 2* math.pi * self.radius
    
class Rectangle(Shape):

    def __init__(self , length , breadth):
        self.length = length 
        self.breadth = breadth
    
    def area(self):
        return self.length*self.breadth
    
    def perimenter(self):
        return (self.length + self.breadth)*2

