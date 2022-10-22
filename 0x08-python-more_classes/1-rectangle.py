#!/usr/bin/python3
"""Module with an empty class"""


class Rectangle:
    """This is a class that defines a square
        Attributes: width (int)
                    height (int)"""
    def __init__(self, width=0, height=0):
        """Initialises instance attribute
            Args: width - Width of rectangle
                  height - Height of rectangle"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieves width parameter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of width"""
        if not (isinstance(value, int)):
            raise TypeError("width must be an integer")
        if value < 0:
                raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves height parameter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of height"""
        if not (isinstance(value, int)):
            raise TypeError("height must be an integer")
        if value < 0:
                raise ValueError("height must be >= 0")
        self.__height = value
