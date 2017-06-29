#!/usr/bin/env python

from dev_ops.linux import get_ipv6_addresses

def linux_get_ipv6_addresses():
    def decorator(connection):
        def wrapper(connection):
            '''
            Summary:
            Return a JSON formatted output of ifconfig containing interface
            IPv6 link local and global addresses.

            Arguments:
            connection:         object, MossDeviceOrchestrator

            Returns:
            dict
            '''

            task_info = {
                'namespace': 'ipv6',
                'task': 'get_ipv6_addresses',
                'platform': 'linux',
                'subtool': 'native'
            }

            output_dict = get_ipv6_addresses(connection)
            output_dict.update(task_info)

            return output_dict

        return wrapper
    return decorator
