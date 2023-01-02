#!/usr/bin/python3
"""Module name : base, Class : Base"""


class Base:
    """Base of all other classes
        method: __init__()"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
