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
        _file = cls.__name__ + ".json"
        with open(_file, "w") as f:
            if list_objs is None:
                return f.write(cls.to_json_string(None))
            stri = []
            for i in list_objs:
                stri.append(cls.to_dictionary(i))
            return f.write(cls.to_json_string(stri))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ == "Square":
            dummy = cls()
        if cls.__name__ == "Rectangle":
            dummy = cls()
        dummy.update(**dictionary)
        return dummy
