#!/usr/bin/python3
"""

the first class Base

"""
import json


class Base:
    """

     the first class Base

    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or not list_dictionaries:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        _file = type(cls).__name__ + ".json"
        stri = []
        if list_objs is not None:
            for j in lists_objs:
                stri.append(cls.to_dictionary(j))
        with open(_file, "w") as f:
            f.write(cls.to_json_string(stri))
