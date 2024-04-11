#!/usr/bin/python3
class Rectangle:
    num_of_instance = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        type(self).num_of_instance += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''
        else:
            rectangle_str = ''
            for _ in range(self.__height):
                rectangle_str += str(print_symbol) * self.__width + '\n'
            return rectangle_str.rstrip()
    def __repr__(self):
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        type(self).num_of_instance -= 1
    print("Bye rectangle...")
