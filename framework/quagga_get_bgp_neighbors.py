#!/usr/bin/env python

from dev_ops.quagga import get_bgp_neighbors

def quagga_get_bgp_neighbors():
    def decorator(connection):
        def wrapper(connection):
            '''
            Summary:
            Return BGP neighbor information in JSON.

            Arguments:
            connection:         object, MossDeviceOrchestrator

            Returns:
            dict
            '''

            task_info = {
                'namespace': 'bgp',
                'task': 'get_bgp_neighbors',
                'platform': 'linux',
                'subtool': 'quagga'
            }

            output_dict = get_bgp_neighbors(connection)
            output_dict.update(task_info)

            return output_dict

        return wrapper
    return decorator
