#!/usr/bin/python3
"""function that loads an obj from a file json string"""
import json


def load_from_json_file(filename=""):
    """load json file"""
    with open(filename, "r") as f:
        return json.load(f)
