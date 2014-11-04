'''
Jake Martin
CSET 1100 - 002
Chapter 07
Exercise 7.05
Geometry: n-sided regular polygon
'''

# Import the math module
import math

# Define main
def main():
    p1 = RegularPolygon()
    print (p1.getPerimeter(), p1.getArea())
    p2 = RegularPolygon(6, 4)
    print (p2.getPerimeter(), p2.getArea())
    p3 = RegularPolygon(10, 4, 5.6, 7.8)
    print (p3.getPerimeter(), p3.getArea())

# Define class, RegularPolygon
class RegularPolygon:
    def __init__(self, n=3, side=1, x=0, y=0): # Constructor, including default parameters
        self.__n = n # Data field for number of sides
        self.__side = side # Data field for length of a side
        self.__x = x # Data field for x-coordinate
        self.__y = y # Data field for y-coordinate

# Define Accessors or "getters"       
    def getN(self): # Get n value
        return self.__n
    
    def getSide(self): # Get side value
        return self.__side
    
    def getX(self): # Get x value
        return self.__x
    
    def getY(self): # Get y value
        return self.__y

# Define Mutators or "setters"   
    def setN(self, n): # Set n value
        self.__n = n
        
    def setSide(self, side): # Set side value
        self.__side = side
        
    def setX(self, x): # Set x value
        self.__x = x
        
    def setY(self, y): # Set y value
        self.__y = y

# Define method for calculating perimeter of polygon
    def getPerimeter(self):
        return self.__side * self.__n
    
# Define method for calculating area of polygon
    def getArea(self):
        return (self.__n * (self.__side ** 2)) / (4 * math.tan(math.pi / self.__n))
    
if __name__ == "__main__":
    main()