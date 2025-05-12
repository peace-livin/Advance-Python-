# Absract class :partly implemented class
# Any python which is chaild of ABC class is called abstract class in python
# ABC class is present inside abc module


from abc import ABC,abstractmethod
#abc module is present inside python
#ABC is a class which is present inside abc module
#abstract method is a method which is present inside abc module
#abstract method is a method which is present inside abc module
from abc import * 
# class Test(ABC):
#     def m1(self):
#         print("m1()")
        
# t=Test()
# t.m1()

# # ex2. 

# class Test:
#     def m1(self):
#         print("m1()")
#     @abstractmethod
#     def m2(self):
#         pass
    
# t=Test()
# t.m1()
# t.m2()

# # ex3.


# class Test(ABC):
#     def m1(self):
#         print("m1()")
#     @abstractmethod
#     def m2(self):
#         pass



from abc import *

# class Greet(ABC):
#     def  wish (self):
#         print("Quality software wishing you")
        
#     @abstractmethod
#     def greet(self):
#         pass
    
# class Diwali(Greet):
#     def greet(self):
#         print("Happy Diwali")
        
# class Holi(Greet):
#     def greet(self):
#         print("Happy Holi")
        
# d=Diwali()
# d.wish()
# d.greet()

# print("<------------>")

# h=Holi()
# h.wish()
# h.greet()

# class Shape(ABC):
#     def area(self):
#         print("Area of shape")
        
        
        
        
#     @abstractmethod
#     def perimeter(self):
#         pass
    
# class circle(Shape):
#     def area(self):
#         print("Area of circle")
    
# class rectangle(Shape):
#     def area(self):
#         print("Area of rectangle")
        
# class tringle(Shape):
#     def area(self):
#         print("Area of triangle")
        
# r=rectangle()
# r.perimeter()
# r.area()

    





from abc import ABC, abstractmethod 
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Triangle(Shape):
    def __init__(self, a, b, c, height):
        self.a = a
        self.b = b
        self.c = c
        self.height = height  # height corresponding to side a

    def area(self):
        return 0.5 * self.a * self.height

    def perimeter(self):
        return self.a + self.b + self.c

# Example usage
r = Rectangle(10, 5)
print("Rectangle Area:", r.area())
print("Rectangle Perimeter:", r.perimeter())

c = Circle(7)
print("Circle Area:", c.area())
print("Circle Perimeter:", c.perimeter())

t = Triangle(5, 6, 7, 4)
print("Triangle Area:", t.area())
print("Triangle Perimeter:", t.perimeter())
