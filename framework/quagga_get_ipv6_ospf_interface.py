#!/usr/bin/env python

from dev_ops.quagga import get_ipv6_ospf_interfaces

def quagga_get_ipv6_ospf_interface():
    def decorator(connection):
        def wrapper(connection, port_id):
            '''
            Summary:
            Returns JSON data for all IPv6 OSPFv3 interfaces and parses
            to find specific interface.

            Arguments:
            connection:         object, MossDeviceOrchestrator
            port_id:            string, target interface

            Returns:
            dict
            '''

            task_info = {
                'namespace': 'ospf',
                'task': 'get_ipv6_ospf_interface',
                'platform': 'linux',
                'subtool': 'quagga'
            }

            output_dict = get_ipv6_ospf_interfaces(connection)
            interface_dict = {}

            for interface in output_dict['stdout']:
                if interface == port_id:
                    interface_dict[interface] = {}
                    interface_dict[interface] = output_dict['stdout'][interface]

            output_dict['stdout'] = interface_dict
            output_dict.update(task_info)
            return output_dict

        return wrapper
    return decorator
