#!/usr/bin/python3
"""Defines the available attributes/methods of an object."""


def lookup(obj):
    """Returns a list of available attributes."""
    return (dir(obj))
