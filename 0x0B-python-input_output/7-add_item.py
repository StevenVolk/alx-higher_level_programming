#!/usr/bin/python3
"""

Using function save_to_json_file from 5-save_to_json_file.py

"""

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

"""

Using function load_from_json_file from 6-load_from_json_file.py

"""

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

"""

importing sys

"""

import sys

"""

a script that adds all arguments to a Python list,
and then save them to a file

"""


def add_items_to_json_file():
    """

    a script that adds all arguments to a Python list,
    and then save them to a file

    """

    p_list = []

    for i in (1, len(sys.argv)):
        p_list.append(sys.argv[i])

    my_list = load_from_json_file('add_item.json')
    mylist.extend(p_list)
    save_to_json_file(my_list, 'add_item.json')

"""

calling function

"""

add_items_to_json_file()
