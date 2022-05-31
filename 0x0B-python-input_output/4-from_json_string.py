#!/usr/bin/python3
"""function that loads an obj from a json strign"""
import json


def from_json_string(my_str):
    """string in json to python dict(obj)"""
    return json.loads(my_str)
