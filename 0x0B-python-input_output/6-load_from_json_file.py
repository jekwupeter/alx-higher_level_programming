#!/usr/bin/python3
"""Module defines a fucntion that converts a json strign to an object"""
import json
def load_from_json_file(filename):
    """creates an object from a json file

    Args:
        filename: name of file to create or edit

    Returns:
        an object of converted json string
    """
    with open(filename, mode="r") as f:
        json_str = f.read()
        obj = json.loads(json_str)
    return obj
