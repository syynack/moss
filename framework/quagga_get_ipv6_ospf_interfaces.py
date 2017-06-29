#!/usr/bin/env python

from dev_ops.quagga import get_ipv6_ospf_interfaces

def quagga_get_ipv6_ospf_interfaces():
    def decorator(connection):
        def wrapper(connection):
            '''
            Summary:
            Returns JSON data for all IPv6 OSPFv3 interfaces.

            Arguments:
            connection:         object, MossDeviceOrchestrator

            Returns:
            dict
            '''

            task_info = {
                'namespace': 'ospf',
                'task': 'get_ipv6_ospf_interfaces',
                'platform': 'linux',
                'subtool': 'quagga'
            }

            output_dict = get_ipv6_ospf_interfaces(connection)
            output_dict.update(task_info)

            return output_dict

        return wrapper
    return decorator
