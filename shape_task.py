import math

class Shape():
    count = 0
    def __init__(self,name,color,d1,d2):
        self.__name = name
        self.__color = color
        self.__d1 = d1
        self.__d2 = d2
        Shape.count = Shape.count + 1 
    def __str__(self):
        return self.__name
    
    def area(self):
        return self.__d1*self.__d2


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__('circle',color,0,0)
        self.__radius = radius
        
    
    def area(self):
        return math.pi*(self.__radius**2)
    

    
        