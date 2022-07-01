#!/usr/bin/python3
"""Module defines an empty rectangle class"""
class Rectangle:
    """defines a rectangle"""
    number_of_instances = 0
    print_symbol = '#'
    def __init__(self, width=0, height=0):
        """Instatiation of attibutes"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width getter property"""
        return(self.__width)

    @width.setter
    def width(self, value):
        """sets the width propety"""
        if not isinstance(self.__width, int):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter property"""
        return(self.__height)

    @width.setter
    def height(self, value):
        """sets the height propety"""
        if not isinstance(self.__height, int):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0

        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """returns printable format of rectangle"""
        return ("\n".join(["".join([str(self.print_symbol) for i in range(self.__width)]) for j in range(self.__height)]))

    def __repr__(self):
        """returns string representation of rectangle"""
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        """custom function to run on delete of instance"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """checks for which rectangle instance is biggest
        
        Args:
            rect_1 (Rectangle): input rectangle instance
            rect_2 (Rectangle): input rectangle instance
        
        Returns:
            biggest rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() > rect_2.area():
            return rect_1

        elif rect_2.area() > rect_1.area():
            return rect_2

        else:
            return rect_1
    
    def square(cls, size=0):
        """creates a new square model instance

        Args:
            size (int): size of rectangle

        Returns:
            a retangle with width == height == size
        """
        return (Rectangle(size, size))
