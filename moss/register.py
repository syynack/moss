#! /usr/bin/env python

REGISTER = {}

def register(platform):
    '''
    Summary:
    Takes modules registered with the @register decorator. Aim is to only allow
    registered modules to be executed. The modules are appended to a list
    which is ordered by platform.

    Arguments:
    platform        string, platform module is intended to be used for

    Returns:
    func
    '''

    def decorator(func):
        if platform:
            if not REGISTER.get(platform):
                REGISTER[platform] = {}
            try:
                REGISTER[platform].update({func.__name__: func})
            except:
                pass
        return func
    return decorator
