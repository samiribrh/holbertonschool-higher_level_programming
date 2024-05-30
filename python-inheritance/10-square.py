#!/usr/bin/python3
"""Module containing BaseGeometry class functions"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class based on BaseGeometry class"""

    def __init__(self, width, height) -> None:
        """Initializing for Rectangle object"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Area calculator function"""
        return self.__width * self.__height

    def __str__(self):
        """Printing the Rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """Square class based on Rectangle class"""

    def __init__(self, size):
        """Initializing for Square object"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
