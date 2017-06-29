#!/usr/bin/env python

from dev_ops.linux import get_lldp_neighbors

def linux_get_lldp_interface():
    def decorator(connection):
        def wrapper(connection, port_id):
            '''
            Summary:
            Return JSON formatted output of the Linux LLDP implementation
            lldpd, for a specific interface

            Arguments:
            connection:         object, MossDeviceOrchestrator
            port_id:            string, interface port ID

            Returns:
            dict
            '''

            task_info = {
                'namespace': 'lldp',
                'task': 'get_lldp_interface',
                'platform': 'linux',
                'subtool': 'lldpd'
            }

            output_dict = get_lldp_neighbors(connection)

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
