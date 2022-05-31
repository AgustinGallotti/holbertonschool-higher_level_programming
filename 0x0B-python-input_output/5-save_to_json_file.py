#!/usr/bin/python3
"""funtion that saves an obj to a file as json string"""
import json


def save_to_json_file(my_obj, filename):
    """mode w, create a new file if one with the same name doesn't exist"""
    with open(filename, "w") as f:
        """method dump is used when an object hace to be stored in a file"""
        json.dump(my_obj, f)
