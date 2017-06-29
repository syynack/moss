#!/usr/bin/env python

from dev_ops.quagga import get_bgp_neighbors

def quagga_get_bgp_neighbor():
    def decorator(connection):
        def wrapper(connection, neighbor_address):
            '''
            Summary:
            Return information for a BGP neighbor in JSON

            Arguments:
            connection:         object, MossDeviceOrchestrator
            neighbor_address:   string, IP address of neighbor

            Returns:
            dict
            '''

            task_info = {
                'namespace': 'bgp',
                'task': 'get_bgp_neighbor',
                'platform': 'linux',
                'subtool': 'quagga'
            }

            output_dict = get_bgp_neighbors(connection)

            if output_dict['result'] == 'fail':
                output_dict.update(task_info)
                return output_dict

            neighbor_dict = {}

            for neighbor in output_dict['stdout']:
                if neighbor == neighbor_address:
                    neighbor_dict[neighbor_address] = output_dict['stdout'][neighbor]

            output_dict['stdout'] = neighbor_dict
            output_dict.update(task_info)
            return output_dict

        return wrapper
    return decorator
