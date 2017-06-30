#!/usr/bin/env python

from dev_ops.quagga import get_bgp_memory_usage, get_bgp_neighbors, get_bgp_summary, \
                           get_interfaces_description, get_ipv6_bgp_routes, \
                           get_ipv6_ospf_interfaces, get_ipv6_ospf_neighbors_brief, \
                           get_ipv6_ospf_neighbors_detail, get_ipv6_ospf_routes, \
                           get_ipv6_rib_routes

def quagga_get_bgp_memory_usage():
    '''
    Summary:
    Returns current memory usage consumed by the Quagga
    BGP daemon bgpd.

    Arguments:
    connection:         object, MossDeviceOrchestrator

    Returns:
    dict
    '''

    def decorator(connection):
        def wrapper(connection):
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


def quagga_get_bgp_neighbor():
    '''
    Summary:
    Return information for a BGP neighbor in JSON

    Arguments:
    connection:         object, MossDeviceOrchestrator
    neighbor_address:   string, IP address of neighbor

    Returns:
    dict
    '''

    def decorator(connection):
        def wrapper(connection, neighbor_address):
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


def quagga_get_bgp_neighbors():
    '''
    Summary:
    Return BGP neighbor information in JSON.

    Arguments:
    connection:         object, MossDeviceOrchestrator

    Returns:
    dict
    '''

    def decorator(connection):
        def wrapper(connection):
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


def quagga_get_bgp_summary():
    '''
    Summary:
    Return summary of BGP peers in JSON.

    Arguments:
    connection:         object, MossDeviceOrchestrator

    Returns:
    dict
    '''

    def decorator(connection):
        def wrapper(connection):
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


def quagga_get_interface_description():
    '''
    Summary:
    Returns JSON formatted data for a Quagga interface.

    Arguments:
    connection:         object, MossDeviceOrchestrator
    port_id:            string, interface port ID

    Returns:
    dict
    '''

    def decorator(connection):
        def wrapper(connection, port_id):
            task_info = {
                'namespace': 'interface',
                'task': 'get_interface_description',
                'platform': 'linux',
                'subtool': 'quagga'
            }

            output_dict = get_interfaces_description(connection)

            if output_dict['result'] == 'fail':
                output_dict.update(task_info)
                return output_dict

            interfaces_dict = {}

            for interface in output_dict['stdout']:
                if interface == port_id:
                    interfaces_dict[interface] = output_dict['stdout'][interface]

            output_dict['stdout'] = interfaces_dict
            output_dict.update(task_info)
            return output_dict

        return wrapper
    return decorator


def quagga_get_interfaces_description():
    '''
    Summary:
    Returns JSON formatted data for Quagga interfaces.

    Arguments:
    connection:         object, MossDeviceOrchestrator

    Returns:
    dict
    '''

    def decorator(connection):
        def wrapper(connection):
            task_info = {
                'namespace': 'interface',
                'task': 'get_interfaces_description',
                'platform': 'linux',
                'subtool': 'quagga'
            }

            output_dict = get_interfaces_description(connection)
            output_dict.update(task_info)

            return output_dict

        return wrapper
    return decorator


def quagga_get_ipv6_bgp_route():
    '''
    Summary:
    Runs vtysh -c "show ipv6 route json" to interact with quagga
    to retrieve the current IPv6 route table in JSON. Only routes
    recieved through protocol 'bgp' are returned. Interates through
    returned JSON to find entries that match the prefix.

    Arguments:
    connection:         object, MossDeviceOrchestrator
    prefix              string, prefix

    Returns:
    dict
    '''

    def decorator(connection):
        def wrapper(connection, prefix):
            task_info = {
                'namespace': 'bgp',
                'task': 'get_ipv6_bgp_route',
                'platform': 'linux',
                'subtool': 'quagga'
            }

            output_dict = get_ipv6_bgp_routes(connection)

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


def quagga_get_ipv6_bgp_routes():
    '''
    Summary:
    Runs vtysh -c "show ipv6 route json" to interact with quagga
    to retrieve the current IPv6 route table in JSON. Only routes
    recieved through protocol 'bgp' are returned.

    Arguments:
    connection:         object, MossDeviceOrchestrator

    Returns:
    dict
    '''

    def decorator(connection):
        def wrapper(connection):
            task_info = {
                'namespace': 'bgp',
                'task': 'get_ipv6_bgp_routes',
                'platform': 'linux',
                'subtool': 'quagga'
            }

            output_dict = get_ipv6_bgp_routes(connection)
            output_dict.update(task_info)

            return output_dict

        return wrapper
    return decorator


def quagga_get_ipv6_ospf_interface():
    '''
    Summary:
    Returns JSON data for all IPv6 OSPFv3 interfaces and parses
    to find specific interface.

    Arguments:
    connection:         object, MossDeviceOrchestrator
    port_id:            string, target interface

    Returns:
    dict
    '''

    def decorator(connection):
        def wrapper(connection, port_id):
            task_info = {
                'namespace': 'ospf',
                'task': 'get_ipv6_ospf_interface',
                'platform': 'linux',
                'subtool': 'quagga'
            }

            output_dict = get_ipv6_ospf_interfaces(connection)

            if output_dict['result'] == 'fail':
                output_dict.update(task_info)
                return output_dict

            interface_dict = {}

            for interface in output_dict['stdout']:
                if interface == port_id:
                    interface_dict[interface] = {}
                    interface_dict[interface] = output_dict['stdout'][interface]

            output_dict['stdout'] = interface_dict
            output_dict.update(task_info)
            return output_dict

        return wrapper
    return decorator


def quagga_get_ipv6_ospf_interfaces():
    '''
    Summary:
    Returns JSON data for all IPv6 OSPFv3 interfaces.

    Arguments:
    connection:         object, MossDeviceOrchestrator

    Returns:
    dict
    '''

    def decorator(connection):
        def wrapper(connection):
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


def quagga_get_ipv6_ospf_neighbor_brief():
    '''
    Summary:
    Return JSON data for a specific OSPFv3 neighbor in a brief format.

    Arguments:
    connection:         object, MossDeviceOrchestrator
    neighbor_rid:       string, OSPFv3 neighbor Router ID

    Returns:
    dict
    '''

    def decorator(connection):
        def wrapper(connection, neighbor_rid):
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


def quagga_get_ipv6_ospf_neighbor_detail():
    '''
    Summary:
    Return JSON data for a specific OSPFv3 neighbor in a detailed format.

    Arguments:
    connection:         object, MossDeviceOrchestrator
    neighbor_rid:       string, OSPFv3 neighbor Router ID

    Returns:
    dict
    '''

    def decorator(connection):
        def wrapper(connection, neighbor_rid):
            task_info = {
                'namespace': 'ospf',
                'task': 'get_ipv6_ospf_neighbor_detail',
                'platform': 'linux',
                'subtool': 'quagga'
            }

            output_dict = get_ipv6_ospf_neighbors_detail(connection)

            if output_dict['result'] == 'fail':
                output_dict.update(task_info)
                return output_dict

            neighbors_dict = {}

            for neighbor in output_dict['stdout']:
                if neighbor == neighbor_rid:
                    neighbors_dict[neighbor] = {}
                    neighbors_dict[neighbor].update(output_dict['stdout'][neighbor])

            output_dict['stdout'] = neighbors_dict
            output_dict.update(task_info)
            return output_dict

        return wrapper
    return decorator


def quagga_get_ipv6_ospf_neighbors_brief():
    '''
    Summary:
    Returns JSON data for all IPv6 OSPFv3 neighbors in a brief format.

    Arguments:
    connection:         object, MossDeviceOrchestrator

    Returns:
    dict
    '''

    def decorator(connection):
        def wrapper(connection):
            task_info = {
                'namespace': 'ospf',
                'task': 'get_ipv6_ospf_neighbors_brief',
                'platform': 'linux',
                'subtool': 'quagga'
            }

            output_dict = get_ipv6_ospf_neighbors_brief(connection)
            output_dict.update(task_info)

            return output_dict

        return wrapper
    return decorator


def quagga_get_ipv6_ospf_neighbors_detail():
    '''
    Summary:
    Returns JSON data for all IPv6 OSPFv3 neighbors in a detailed format.

    Arguments:
    connection:         object, MossDeviceOrchestrator

    Returns:
    dict
    '''

    def decorator(connection):
        def wrapper(connection):
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


def quagga_get_ipv6_ospf_route():
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

    def decorator(connection):
        def wrapper(connection, prefix):
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


def quagga_get_ipv6_ospf_routes():
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

    def decorator(connection):
        def wrapper(connection):
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


def quagga_get_ipv6_rib_route():
    '''
    Summary:
    Runs vtysh -c "show ipv6 route json" to interact with quagga
    to retrieve the current IPv6 route table in JSON.

    Arguments:
    connection:         object, MossDeviceOrchestrator

    Returns:
    dict
    '''

    def decorator(connection):
        def wrapper(connection, prefix):
            task_info = {
                'namespace': 'rib',
                'task': 'get_ipv6_rib_route',
                'platform': 'linux',
                'subtool': 'quagga'
            }

            output_dict = get_ipv6_rib_routes(connection)

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


def quagga_get_ipv6_rib_routes():
    '''
    Summary:
    Runs vtysh -c "show ipv6 route json" to interact with quagga
    to retrieve the current IPv6 route table in JSON.

    Arguments:
    connection:         object, MossDeviceOrchestrator

    Returns:
    dict
    '''

    def decorator(connection):
        def wrapper(connection):
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
