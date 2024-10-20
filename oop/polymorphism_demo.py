# polymorphism_demo.py
import math

# Base class - Shape


class Shape:
    def area(self):
        """Method to be overridden in derived classes"""
        raise NotImplementedError(
            "The area() method must be overridden in derived classes")

# Derived class - Rectangle


class Rectangle(Shape):
    def __init__(self, length, width):
        """Initializes a Rectangle with length and width"""
        self.length = length
        self.width = width

    def area(self):
        """Calculates the area of a rectangle"""
        return self.length * self.width

# Derived class - Circle


class Circle(Shape):
    def __init__(self, radius):
        """Initializes a Circle with radius"""
        self.radius = radius

    def area(self):
        """Calculates the area of a circle"""
        return math.pi * (self.radius ** 2)
