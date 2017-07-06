#!/usr/bin/env python

from .quagga import quagga_get_bgp_memory_usage, quagga_get_bgp_neighbor, \
                    quagga_get_bgp_neighbors, quagga_get_bgp_summary, \
                    quagga_get_interface_description, quagga_get_interfaces_description, \
                    quagga_get_ipv6_ospf_interface, quagga_get_ipv6_ospf_interfaces, \
                    quagga_get_ipv6_ospf_neighbor_brief, quagga_get_ipv6_ospf_neighbor_detail, \
                    quagga_get_ipv6_ospf_neighbors_brief, quagga_get_ipv6_ospf_neighbors_detail, \
                    quagga_get_ipv6_route_table


from .linux import linux_get_interface_statistics, linux_get_interfaces_mac_address, \
                   linux_get_interfaces_statistics, linux_get_ipv6_addresses, \
                   linux_get_lldp_interface, linux_get_lldp_neighbors, linux_get_ndp_table_reachable_entries, \
                   linux_get_ndp_table_stale_entries, linux_get_ndp_table, linux_get_system_info, \
                   linux_get_system_uptime

'''
target_mod = __import__(device_type)
target_func = getattr(target_mod, sys._getframe().f_code.co_name)
return target_func()
'''


def get_bgp_memory_usage():
    def decorator(connection):
        def wrapper(connection):
            device_type = connection.device_type

            if device_type == 'linux':
                return quagga_get_bgp_memory_usage(connection)

        return wrapper
    return decorator


def get_bgp_neighbor():
    def decorator(connection):
        def wrapper(connection, neighbor_address):
            device_type = connection.device_type

            if device_type == 'linux':
                return quagga_get_bgp_neighbor(connection, neighbor_address)

        return wrapper
    return decorator


def get_bgp_neighbors():
    def decorator(connection):
        def wrapper(connection):
            device_type = connection.device_type

            if device_type == 'linux':
                return quagga_get_bgp_neighbors(connection)

        return wrapper
    return decorator


def get_bgp_summary():
    def decorator(connection):
        def wrapper(connection):
            device_type = connection.device_type

            if device_type == 'linux':
                return quagga_get_bgp_summary(connection)

        return wrapper
    return decorator


def get_interface_description():
    def decorator(connection):
        def wrapper(connection, port_id):
            device_type = connection.device_type

            if device_type == 'linux':
                return quagga_get_interface_description(connection, port_id)

        return wrapper
    return decorator


def get_interfaces_description():
    def decorator(connection):
        def wrapper(connection):
            device_type = connection.device_type

            if device_type == 'linux':
                return quagga_get_interfaces_description(connection)

        return wrapper
    return decorator


def get_interface_statistics():
    def decorator(connection):
        def wrapper(connection, port_id):
            device_type = connection.device_type

            if device_type == 'linux':
                return linux_get_interface_statistics(connection, port_id)

        return wrapper
    return decorator


def get_interfaces_statistics():
    def decorator(connection):
        def wrapper(connection):
            device_type = connection.device_type

            if device_type == 'linux':
                return linux_get_interfaces_statistics(connection)

        return wrapper
    return decorator


def get_interfaces_mac_address():
    def decorator(connection):
        def wrapper(connection):
            device_type = connection.device_type

            if device_type == 'linux':
                return linux_get_interfaces_mac_address(connection)

        return wrapper
    return decorator


def get_ipv6_addresses():
    def decorator(connection):
        def wrapper(connection):
            device_type = connection.device_type

            if device_type == 'linux':
                return linux_get_ipv6_addresses(connection)

        return wrapper
    return decorator


def get_ipv6_ospf_interface():
    def decorator(connection):
        def wrapper(connection, port_id):
            device_type = connection.device_type

            if device_type == 'linux':
                return quagga_get_ipv6_ospf_interface(connection, port_id)

        return wrapper
    return decorator


def get_ipv6_ospf_interfaces():
    def decorator(connection):
        def wrapper(connection):
            device_type = connection.device_type

            if device_type == 'linux':
                return quagga_get_ipv6_ospf_interfaces(connection)

        return wrapper
    return decorator


def get_ipv6_ospf_neighbor_brief():
    def decorator(connection):
        def wrapper(connection, neighbor_rid):
            device_type = connection.device_type

            if device_type == 'linux':
                return quagga_get_ipv6_ospf_neighbor_brief(connection, neighbor_rid)

        return wrapper
    return decorator


def get_ipv6_ospf_neighbor_detail():
    def decorator(connection):
        def wrapper(connection, neighbor_rid):
            device_type = connection.device_type

            if device_type == 'linux':
                return quagga_get_ipv6_ospf_neighbor_detail(connection, neighbor_rid)

        return wrapper
    return decorator


def get_ipv6_ospf_neighbors_brief():
    def decorator(connection):
        def wrapper(connection):
            device_type = connection.device_type

            if device_type == 'linux':
                return quagga_get_ipv6_ospf_neighbors_brief(connection)

        return wrapper
    return decorator


def get_ipv6_ospf_neighbors_detail():
    def decorator(connection):
        def wrapper(connection):
            device_type = connection.device_type

            if device_type == 'linux':
                return quagga_get_ipv6_ospf_neighbors_detail(connection)

        return wrapper
    return decorator


def get_ipv6_route_table():
    def decorator(connection):
        def wrapper(connection):
            device_type = connection.device_type

            if device_type == 'linux':
                return quagga_get_ipv6_route_table(connection)

        return wrapper
    return decorator


def get_lldp_interface():
    def decorator(connection):
        def wrapper(connection, port_id):
            device_type = connection.device_type

            if device_type == 'linux':
                return linux_get_lldp_interface(connection, port_id)

        return wrapper
    return decorator


def get_lldp_neighbors():
    def decorator(connection):
        def wrapper(connection):
            device_type = connection.device_type

            if device_type == 'linux':
                return linux_get_lldp_neighbors(connection)

        return wrapper
    return decorator

def get_ndp_table_reachable_entries():
    def decorator(connection):
        def wrapper(connection):
            device_type = connection.device_type

            if device_type == 'linux':
                return linux_get_ndp_table_reachable_entries(connection)

        return wrapper
    return decorator


def get_ndp_table_stale_entries():
    def decorator(connection):
        def wrapper(connection):
            device_type = connection.device_type

            if device_type == 'linux':
                return linux_get_ndp_table_stale_entries(connection)

        return wrapper
    return decorator


def get_ndp_table():
    def decorator(connection):
        def wrapper(connection):
            device_type = connection.device_type

            if device_type == 'linux':
                return linux_get_ndp_table(connection)

        return wrapper
    return decorator


def get_system_info():
    def decorator(connection):
        def wrapper(connection):
            device_type = connection.device_type

            if device_type == 'linux':
                return linux_get_system_info(connection)

        return wrapper
    return decorator


def get_system_uptime():
    def decorator(connection):
        def wrapper(connection):
            device_type = connection.device_type

            if device_type == 'linux':
                return linux_get_system_uptime(connection)

        return wrapper
    return decorator
