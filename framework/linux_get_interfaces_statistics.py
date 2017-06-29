#!/usr/bin/env python

from dev_ops.linux import get_interfaces_statistics

def linux_get_interfaces_statistics():
    def decorator(connection):
        def wrapper(connection):
            '''
            Summary:
            Returns detailed statistics JSON formatted data for Linux interfaces

            Arguments:
            connection:         object, MossDeviceOrchestrator

            Returns:
            dict
            '''

            task_info = {
                'namespace': 'interface',
                'task': 'get_interfaces_statistics',
                'platform': 'linux',
                'subtool': 'native'
            }

            output_dict = get_interfaces_statistics(connection)
            output_dict.update(task_info)

            return output_dict

        return wrapper
    return decorator
