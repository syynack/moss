#!/usr/bin/env python

from dev_ops.linux import get_ndp_table

def linux_get_ndp_table():
    def decorator(connection):
        def wrapper(connection):
            '''
            Summary:
            Returns the IPv6 Neighbor Discovery Protocol table in a JSON format.

            Arguments:
            connection:         object, MossDeviceOrchestrator

            Returns:
            dict
            '''

            task_info = {
                'namespace': 'ndp',
                'task': 'get_ndp_table',
                'platform': 'linux',
                'subtool': 'native'
            }

            output_dict = get_ndp_table(connection)
            output_dict.update(task_info)

            return output_dict

        return wrapper
    return decorator
