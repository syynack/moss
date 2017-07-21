#!/usr/bin/env python

import sys
import socket
import os
import getpass
import inspect
import moss.devops

from datetime import datetime
from moss.register import registered_operations
from moss.utils import timer, module_start_header, module_success, module_branch, module_abort, module_fail


def execute_device_operation(operation, connection):
    try:
        return registered_operations['devops'][connection.device_type][operation](connection)
    except:
        raise


def module(module_name, **kwargs):
    def _decorator(func):
        def wrapper(connection):
            device_type = connection.device_type
            return registered_operations['modules'][device_type][module_name](connection, **kwargs)
        return wrapper
    return _decorator


def _module_start_signals(module):
    module_start_header(module)

    return {
        'start_time': timer(),
        'start_date_time': str(datetime.now())
    }


class ModuleResult():

    def __init__(self):
        pass


    @staticmethod
    def abort():
        return {
            'result': 'abort'
        }


    @staticmethod
    def branch(module):
        return {
            'result': 'branch',
            'branching_module': module
        }


    @staticmethod
    def fail():
        return {
            'result': 'fail'
        }


    @staticmethod
    def success():
        return {
            'result': 'success'
        }


class Module():

    def __init__(self, connection = None, module = '', next_module = ''):
        self.connection = connection
        self.module = module
        self.next_module = next_module


    def run(self):
        self.module_start_data = self._module_start_signals(self.module)
        try:
            module_result = registered_operations['modules'][self.connection.device_type][self.module](self.connection)
        except:
            raise

        if isinstance(module_result, dict):
            return self._module_result(module_result)
        elif callable(module_result):
            return self._module_result(module_result())


    def _module_start_signals(self, module):
        module_start_header(module)

        return {
            'start_time': timer(),
            'start_date_time': str(datetime.now())
        }


    def _module_result(self, module_result):
        result = module_result['result']
        result_dict = {
            'result': result,
            'end_time': timer(),
            'run_time': timer() - self.module_start_data['start_time'],
            'end_date_time': str(datetime.now())
        }
        result_dict.update(self.module_start_data)

        if result == 'success':
            result_dict.update({'next_module': self.next_module})
            module_success()
        elif result == 'branch':
            result_dict.update({'next_module': module_result['branching_module']})
            module_branch(module_result['branching_module'])
        elif result == 'abort':
            result_dict.update({'next_module': ''})
            module_abort()
        elif result == 'fail':
            module_fail()
            result_dict.update({'next_module': ''})

        return result_dict
