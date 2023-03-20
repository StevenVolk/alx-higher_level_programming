#!/usr/bin/python3
"""

importing json function

"""

import json

"""

A function that creates an Object from a “JSON file”

"""


def load_from_json_file(filename):
    """

    A function that creates an Object from a “JSON file”

    """

    with open(filename, 'r') as f:
        return json.loads(f.read())
