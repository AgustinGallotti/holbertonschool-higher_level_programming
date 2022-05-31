#!/usr/bin/python3
"""list from args and save in a file json format"""
import sys
import json


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    listt = load_from_json_file()
except FileNotFoundError:
    listt = []
for arg in sys.argv[1:]:
    """values that are passed during calling of program
    along with thecalling statement"""
    listt.append(add_item)
save_to_json_file(listt, add_item)
