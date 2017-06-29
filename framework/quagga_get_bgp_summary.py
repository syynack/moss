#!/usr/bin/env python

from dev_ops.quagga import get_bgp_summary

def quagga_get_bgp_summary():
    def decorator(connection):
        def wrapper(connection):
            '''
            Summary:
            Return summary of BGP peers in JSON.

            Arguments:
            connection:         object, MossDeviceOrchestrator

            Returns:
            dict
            '''

            task_info = {
                'namespace': 'bgp',
                'task': 'get_bgp_summary',
                'platform': 'linux',
                'subtool': 'quagga'
            }

            output_dict = get_bgp_summary(connection)
            output_dict.update(task_info)

            return output_dict

        return wrapper
    return decorator
