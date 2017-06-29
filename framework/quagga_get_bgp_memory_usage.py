#!/usr/bin/env python

from dev_ops.quagga import get_bgp_memory_usage

def quagga_get_bgp_memory_usage():
    def decorator(connection):
        def wrapper(connection):
            '''
            Summary:
            Returns current memory usage consumed by the Quagga
            BGP daemon bgpd.

            Arguments:
            connection:         object, MossDeviceOrchestrator

            Returns:
            dict
            '''

            task_info = {
                'namespace': 'bgp',
                'task': 'get_bgp_memory_usage',
                'platform': 'linux',
                'subtool': 'quagga'
            }

            output_dict = get_bgp_memory_usage(connection)
            output_dict.update(task_info)

            return output_dict

        return wrapper
    return decorator
