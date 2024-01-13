#!/usr/bin/python3

def add(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Must be integer")
    return a + b
