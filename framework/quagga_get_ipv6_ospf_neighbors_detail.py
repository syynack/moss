#!/usr/bin/env python

from dev_ops.quagga import get_ipv6_ospf_neighbors_detail

def quagga_get_ipv6_ospf_neighbors_detail():
    def decorator(connection):
        def wrapper(connection):
            '''
            Summary:
            Returns JSON data for all IPv6 OSPFv3 neighbors in a detailed format.

            Arguments:
            connection:         object, MossDeviceOrchestrator

            Returns:
            dict
            '''

            task_info = {
                'namespace': 'ospf',
                'task': 'get_ipv6_ospf_neighbors_detail',
                'platform': 'linux',
                'subtool': 'quagga'
            }

            output_dict = get_ipv6_ospf_neighbors_detail(connection)
            output_dict.update(task_info)

            return output_dict

        return wrapper
    return decorator
