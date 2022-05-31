#!/usr/bin/python3
"""list from args and save in a file json format"""
import sys
import json
savejson = __import__("7-save_to_json_file").save_to_json_file
loadjson = __import__("8-load_from_json_file").load_from_json_file

try:
    listt = loadjson("add_item.json")
except FileNotFoundError:
    listt = []
for arg in sys.argv[1:]:
    """values that are passed during calling of program
    along with thecalling statement"""
    listt.append(arg)
savejson(listt, "add_item.json")
