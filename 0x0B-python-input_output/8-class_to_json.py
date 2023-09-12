#!/usr/bin/python3
""" class-to-JSON module."""


def class_to_json(obj):
    """Returns the dictionary represntation of json."""
    return obj.__dict__
