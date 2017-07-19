#! /usr/bin/env python

from moss.framework.core.registry import registry

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
        if isinstance(platform, str):
            if 'moss.framework.devops.' in str(func.__module__):
                registry('devops', platform, func)
            else:
                registry('modules', platform, func)
        return func
    return decorator


def module(module_name, **kwargs):
    '''
    Summary:
    Allows modules to be run through the use of decorators. For example the user
    can write @moss.module('linux_get_system_uptime', connection) decorating a function
    to return the information.
    '''

    def _decorator(func):
        def wrapper(connection):
            device_type = connection.device_type
            return registered_operations['modules'][device_type][module_name](connection, **kwargs)
        return wrapper
    return _decorator
