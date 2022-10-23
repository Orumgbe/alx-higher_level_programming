#!/usr/bin/python3
"""Module name : 8-base_geometry
   Class : BaseGeometry, Subclass : Rectangle"""


class BaseGeometry:
    """Class with a public instance method:
       'area()' and 'integer_validator()'"""
    def area(self):
        """raises an exception with a message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks if value is a positive integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """class rectangle inherits from 'BaseGeometry'"""
    def __init__(self, width, height):
        """initialises width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__heigth = height
