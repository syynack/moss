#!/usr/bin/env python

from dev_ops.linux import get_lldp_neighbors

def linux_get_lldp_neighbors():
    def decorator(connection):
        def wrapper(connection):
            '''
            Summary:
            Returns JSON formatted output of the lldpd daemon on Linux.

            Arguments:
            connection:         object, MossDeviceOrchestrator

            Returns:
            dict
            '''

            task_info = {
                'namespace': 'lldp',
                'task': 'get_lldp_neighbors',
                'platform': 'linux',
                'subtool': 'lldpd'
            }

            output_dict = get_lldp_neighbors(connection)
            output_dict.update(task_info)

            return output_dict

        return wrapper
    return decorator
