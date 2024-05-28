#!/usr/bin/python3
"""Module containing Rectangle class"""


class Rectangle:
    """Class representing rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialization of Instance"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for __width"""
        return self.__width

    @property
    def height(self):
        """Getter for __height"""
        return self.__height

    @width.setter
    def width(self, value):
        """Setter for width"""

        # Checking if value is not valid
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter for height"""

        # Checking if value is not valid
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method to return area"""
        return self.__height * self.__width

    def perimeter(self):
        """Method to return perimeter"""

        # Checking if height and width is equal to 0
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Method to print the rectangle"""

        # Checking if height and width is equal to 0
        if self.__height == 0 or self.__width == 0:
            print()
        else:

            # Creating string for printing
            rectangle = []
            for i in range(self.__height - 1):
                rectangle.append(self.__width * str(self.print_symbol) + '\n')
            rectangle.append(self.__width * str(self.print_symbol))
            return "".join(rectangle)

    def __repr__(self):
        """Method to return recreateable instance"""

        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Method to print "Bye rectangle..." when an instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Method to compare two Rectangles"""

        # Checking if two given parameters are not the instances of Rectangle
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1


my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(2, 3)

if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")
