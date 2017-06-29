#!/usr/bin/env python

from dev_ops.quagga import get_interfaces_description

def quagga_get_interfaces_description():
    def decorator(connection):
        def wrapper(connection):
            '''
            Summary:
            Returns JSON formatted data for Quagga interfaces.

            Arguments:
            connection:         object, MossDeviceOrchestrator

            Returns:
            dict
            '''

            task_info = {
                'namespace': 'interface',
                'task': 'get_interfaces_description',
                'platform': 'linux',
                'subtool': 'quagga'
            }

            output_dict = get_interfaces_description(connection)
            output_dict.update(task_info)

            return output_dict

        return wrapper
    return decorator
