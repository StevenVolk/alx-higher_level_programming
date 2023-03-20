#!/usr/bin/python3
"""

importing json function

"""

import json

"""

A function that writes an Object to a text file, using a JSON representation

"""


def save_to_json_file(my_obj, filename):
    """

    A function that writes an Object to a text file, using a JSON
    representation

    """

    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
