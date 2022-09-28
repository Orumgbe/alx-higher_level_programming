#!/usr/bin/python3
""" Module with a class 'Square'"""


class Square:
    """Class that defines a square"""
    def __init__(self, size=0, position=(0,0)):
        """initialise for every instance"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrieve attribute 'size'"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set conditions for size attribute"""
        if value < 0:
            raise ValueError("size must be >= 0")
        if type(value) not in [int]:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """Retrieve attribute 'position'"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set conditions for position attribute"""
        if type(value) not in [tuple]:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) not in [int] or type(value[1]) not in [int]:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns area of the square"""
        return self.__size**2

    def my_print(self):
        """prints the square at specified position"""
        length = self.__size
        right = self.__position[0]
        down = self.__position[1]

        if length == 0:
            print()
        else:
            if (down > 0):
                self.__position = 0
                while(down > 0):
                    print()
                    down -= 1
            while(length > 0):
                print(" " * right, end="")
                print("#" * self.__size)
                length -= 1





















