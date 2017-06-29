#!/usr/bin/env python

from dev_ops.quagga import get_ipv6_ospf_routes

def quagga_get_ipv6_ospf_routes():
    def decorator(connection):
        def wrapper(connection):
            '''
            Summary:
            Runs vtysh -c "show ipv6 route json" to interact with quagga
            to retrieve the current IPv6 route table in JSON. Only routes
            recieved through protocol 'ospf6' are returned.

            Arguments:
            connection:         object, MossDeviceOrchestrator

            Returns:
            dict
            '''

            task_info = {
                'namespace': 'ospf',
                'task': 'get_ipv6_ospf_routes',
                'platform': 'linux',
                'subtool': 'quagga'
            }

            output_dict = get_ipv6_ospf_routes(connection)
            output_dict.update(task_info)

            return output_dict

        return wrapper
    return decorator
