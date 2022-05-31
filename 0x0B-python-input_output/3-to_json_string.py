#!/usr/bin/python3
"""funtion that converts an object a json string"""
import json


def to_json_string(my_obj):
    """method dump when obj have to be stored in a file"""
    return json.dumps(my_obj)
