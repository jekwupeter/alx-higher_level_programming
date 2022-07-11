#!/usr/bin/python3
"""Module defines a function that adds all file\
        argument to a list and saves to a file"""
import sys, json, os.path

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

my_list = []

if os.path.exists("add_item.json") and os.path.getsize("add_item.json") > 0:
    my_list = load_from_json_file("add_item.json")

for i in range(1, len(sys.argv)):
    try:
        obj_file = load_from_json_file(sys.argv[i])
        json_txt = json.dumps(json_file)
        ret.append(json_txt)
        continue
    except:
        pass
    try:
        my_list.append(sys.argv[i])
    except:
        pass

save_to_json_file(my_list, "add_item.json")
