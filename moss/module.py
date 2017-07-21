#!/usr/bin/env python

import sys
import os
import moss.modules

from moss.register import REGISTER

def module(module_name, **kwargs):
    def _decorator(func):
        def wrapper(connection):
            device_type = connection.device_type
            return REGISTER[device_type][module_name](connection, **kwargs)
        return wrapper
    return _decorator
