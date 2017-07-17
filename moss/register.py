#! /usr/bin/env python

REGISTER = {}

def register(func):
    platform_name = func.__module__
    platform_name = platform_name.split('.')[-1]

    if platform_name not in REGISTER:
        REGISTER[platform_name] = []
        REGISTER[platform_name].append(func.__name__)
    else:
        REGISTER[platform_name].append(func.__name__)
        
    return func
