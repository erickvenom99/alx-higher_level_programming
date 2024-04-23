#!/usr/bin/python3
"""
Module Defines a Rectangle Model
"""

from base import Base


class Rectangle(Base):
    """
    Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize the Rectangle
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        x getter
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        x setter
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        y getter
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        y setter
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Area of Rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Display Rectangle
        """
        for _ in range(self.y):
            print()

        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Return the string representation of the rectangle
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format( self.id,
                                                        self.__x,
                                                        self.__y,
                                                        self.__width,
                                                        self.__height)
    def update(self, *args, **kwargs):
        """
        update the rectangle arrributes
        """
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for k, att in enumerate(attributes):
                if k < len(args):
                    setattr(self, att, args[k])
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Dictionary representation of a rectangle
        """
        rectangle_dict = {
                "x": self.x,
                "y": self.y,
                "id": self.id,
                "height": self.height,
                "width": self.width
        }
        return rectangle_dict


if __name__ == "__main__":

    r1 = Rectangle(10, 2, 1, 9)
    print(r1)
    r1_dictionary = r1.to_dictionary()
    print(r1_dictionary)
    print(type(r1_dictionary))

    r2 = Rectangle(1, 1)
    print(r2)
    r2.update(**r1_dictionary)
    print(r2)
    print(r1 == r2)
