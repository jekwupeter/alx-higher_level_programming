#!/usr/bin/python3
"""Module defines a fucntion that converts class atribute ot json string"""
import json
def class_to_json(obj):
    """converts JSON serialization of object to dictionary decription
    Args:
        obj: input object

    Returns:
        dictionary description with simple data structure
    """
    json_str = json.loads(json.dumps(obj.__dict__))
    return json_str
