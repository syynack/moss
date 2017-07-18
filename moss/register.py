#! /usr/bin/env python

REGISTER = {}

def register(platform):
    def decorator(func):
        if platform:
            if not REGISTER.get(platform):
                REGISTER[platform] = {}

            REGISTER[platform].update({func.__name__: func})
        return func
    return decorator
