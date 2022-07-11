#!/usr/bin/python3
"""Module defines a fucntions that decodes json"""
import json
def from_json_string(my_str):
    """converts a json string to python object

    Args:
        my_str (str): input json string

    return:
        python data structure representation of json string
    """
    return json.loads(my_str)
