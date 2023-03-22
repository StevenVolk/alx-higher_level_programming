#!/usr/bin/python3
"""

importing json

"""


import json

"""

A class Student that defines a student

"""


class Student:
    """

    A class Student that defines a student

    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        attr_dict = self.__dict__
        attr = dict()

        if attrs is None:
            return attr_dict

        for att in attrs:
            if att in attr_dict:
                attr[att] = attr_dict[att]

        return attr

    def reload_from_json(self, json):
        from_json = json.loads(json)
        self.first_name = from_json[first_name]
        self.last_name = from_json[last_name]
        self.age = from_json[age]
