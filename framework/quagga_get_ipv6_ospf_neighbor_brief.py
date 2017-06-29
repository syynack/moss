#!/usr/bin/env python

from dev_ops.quagga import get_ipv6_ospf_neighbors_brief

def quagga_get_ipv6_ospf_neighbor_brief():
    def decorator(connection):
        def wrapper(connection, neighbor_rid):
            '''
            Summary:
            Return JSON data for a specific OSPFv3 neighbor in a brief format.

            Arguments:
            connection:         object, MossDeviceOrchestrator
            neighbor_rid:       string, OSPFv3 neighbor Router ID

            Returns:
            dict
            '''

            task_info = {
                'namespace': 'ospf',
                'task': 'get_ipv6_ospf_neighbor_brief',
                'platform': 'linux',
                'subtool': 'quagga'
            }

            output_dict = get_ipv6_ospf_neighbors_brief(connection)

            if output_dict['result'] == 'fail':
                output_dict.update(task_info)
                return output_dict

            neighbors_dict = {}

            for neighbor in output_dict['stdout']:
                if neighbor['neighbor_rid'] == neighbor_rid:
                    neighbors_dict.update(neighbor)

            output_dict['stdout'] = neighbors_dict
            output_dict.update(task_info)
            return output_dict

        return wrapper
    return decorator
