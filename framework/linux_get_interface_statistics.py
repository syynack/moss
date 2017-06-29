#!/usr/bin/env python

from dev_ops.linux import get_interfaces_statistics

def linux_get_interface_statistics():
    def decorator(connection):
        def wrapper(connection, port_id):
            '''
            Summary:
            Returns detailed statistics JSON formatted data for a specific Linux
            interface.

            Arguments:
            connection:         object, MossDeviceOrchestrator

            Returns:
            dict
            '''

            task_info = {
                'namespace': 'interface',
                'task': 'get_interface_statistics',
                'platform': 'linux',
                'subtool': 'native'
            }

            output_dict = get_interfaces_statistics(connection)

            if output_dict['result'] == 'fail':
                output_dict.update(task_info)
                return output_dict

            interfaces_dict = {}

            for interface in output_dict['stdout']:
                if interface == port_id:
                    interfaces_dict[interface] = output_dict['stdout'][interface]

            output_dict['stdout'] = interfaces_dict
            output_dict.update(task_info)

            return output_dict

        return wrapper
    return decorator
