#!/usr/bin/python3
"""This script adds all arguments to a list and
saves to a file"""
import json
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


args = sys.argv[1:]
save_to_json_file(args, "add_item.json")
load_from_json_file("add_item.json")
