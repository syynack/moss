#!/usr/bin/env python

from dev_ops.linux import get_interfaces_mac_address

def linux_get_interfaces_mac_address():
    def decorator(connection):
        def wrapper(connection):
            '''
            Summary:
            Returns the MAC address of recognised Linux Kernel interfaces.

            Arguments:
            connection:         object, MossDeviceOrchestrator

            Returns:
            dict
            '''

            task_info = {
                'namespace': 'mac',
                'task': 'get_interfaces_mac_address',
                'platform': 'linux',
                'subtool': 'native'
            }

            output_dict = get_interfaces_mac_address(connection)
            output_dict.update(task_info)

            return output_dict

        return wrapper
    return decorator
