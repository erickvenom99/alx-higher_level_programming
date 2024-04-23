#!/usr/bin/python3
"""
Module defines a square class
"""
from rectangle import Rectangle


class Square(Rectangle):
    """
    Sauare class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for Square  class
        """
        super().__init__(size, size, x, y,  id)

    @property
    def size(self):
        """
        Get square size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set square size
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        set str
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """
        Update Square by adding public method
        """
        if args:
            attributes = ['id', 'size', 'x', 'y']
            for count, arg in enumerate(args):
                if count < len(attributes):
                    setattr(self, attributes[count], arg)
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.width = value
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                else:
                    break

    def to_dictionary(self):
        """
        Dictionary representation of square
        """
        square_dict = {
                    "id": self.id,
                    "x": self.x,
                    "size": self.width,
                    "y": self.width
        }
        return square_dict


if __name__ == "__main__":

    s1 = Square(10, 2, 1)
    print(s1)
    s1_dictionary = s1.to_dictionary()
    print(s1_dictionary)
    print(type(s1_dictionary))

    s2 = Square(1, 1)
    print(s2)
    s2.update(**s1_dictionary)
    print(s2)
    print(s1 == s2)
