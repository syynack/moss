#!/usr/bin/env python

from dev_ops.quagga import get_interfaces_description

def quagga_get_interface_description():
    def decorator(connection):
        def wrapper(connection, port_id):
            '''
            Summary:
            Returns JSON formatted data for a Quagga interface.

            Arguments:
            connection:         object, MossDeviceOrchestrator
            port_id:            string, interface port ID

            Returns:
            dict
            '''

            task_info = {
                'namespace': 'interface',
                'task': 'get_interface_description',
                'platform': 'linux',
                'subtool': 'quagga'
            }

            output_dict = get_interfaces_description(connection)

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
