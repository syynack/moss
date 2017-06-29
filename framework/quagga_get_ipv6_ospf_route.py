#!/usr/bin/env python

from dev_ops.quagga import get_ipv6_ospf_routes

def quagga_get_ipv6_ospf_route():
    def decorator(connection):
        def wrapper(connection, prefix):
            '''
            Summary:
            Runs vtysh -c "show ipv6 route json" to interact with quagga
            to retrieve the current IPv6 route table in JSON. Only routes
            recieved through protocol 'ospf6' are returned. Interates through
            returned JSON to find entries that match the prefix.

            Arguments:
            connection:         object, MossDeviceOrchestrator
            prefix              string, prefix

            Returns:
            dict
            '''

            task_info = {
                'namespace': 'ospf',
                'task': 'get_ipv6_ospf_route',
                'platform': 'linux',
                'subtool': 'quagga'
            }

            output_dict = get_ipv6_ospf_routes(connection)

            if output_dict['result'] == 'fail':
                output_dict.update(task_info)
                return output_dict

            route_dict = {}
            subroute_count = 0

            for route in output_dict['stdout']:
                for subroute in output_dict['stdout'][route]:
                    if prefix in route:
                        route_dict[route] = output_dict['stdout'][route]

            output_dict['stdout'] = route_dict
            output_dict.update(task_info)
            return output_dict

        return wrapper
    return decorator
