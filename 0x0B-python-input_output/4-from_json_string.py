#!/usr/bin/python3

""" Defines from_json_string module """
import json


def from_json_string(my_str):
    """
    Returns a JSON object
    """

    return json.loads(my_str)
