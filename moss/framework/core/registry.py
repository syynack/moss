#! /usr/bin/env python

registered_operations = {'devops': {}, 'modules': {}}

def registry(_type, platform, func):
    if not registered_operations[_type].get(platform):
        registered_operations[_type][platform] = {}
    try:
        registered_operations[_type][platform].update({func.__name__: func})
    except:
        pass
