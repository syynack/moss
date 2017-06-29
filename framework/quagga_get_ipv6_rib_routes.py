#!/usr/bin/env python

from dev_ops.quagga import get_ipv6_rib_routes

def quagga_get_ipv6_rib_routes():
    def decorator(connection):
        def wrapper(connection):
            '''
            Summary:
            Runs vtysh -c "show ipv6 route json" to interact with quagga
            to retrieve the current IPv6 route table in JSON.

            Arguments:
            connection:         object, MossDeviceOrchestrator

            Returns:
            dict
            '''

            task_info = {
                'namespace': 'rib',
                'task': 'get_ipv6_rib_routes',
                'platform': 'linux',
                'subtool': 'quagga'
            }

            output_dict = get_ipv6_rib_routes(connection)
            output_dict.update(task_info)

            return output_dict

        return wrapper
    return decorator
