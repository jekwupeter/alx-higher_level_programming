#!/usr/bin/python3
"""defines a function that returns the json\
        representaiton of an object"""
import json
def to_json_string(my_obj):
    """converts an object to json string"""
    json_str = json.dumps(my_obj)
    return json_str
