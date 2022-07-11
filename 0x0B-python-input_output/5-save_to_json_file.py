#!/usr/bin/python3
"""A module that defines a function that writes a json string to file"""
import json
def save_to_json_file(my_obj, filename):
    """converts python object to json string and writes to file
    
    Args:
        my_obj: input object
        filename: files name of file ot be created or edited
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json_string = json.dumps(my_obj)
        return f.write(json_string)
