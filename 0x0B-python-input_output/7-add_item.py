#!/usr/bin/python3
"""list from args and save in a file json format"""
from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

try:
    listt = load_from_json_file(filename)
except FileNotFoundError:
    listt = []

save_to_json_file(listt + argv[1:], filename)
