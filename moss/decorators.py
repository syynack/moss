#!/usr/bin/env python

import sys

def _run_operation(connection, func_name, *arg):
    device_type = connection.device_type

    target_mod = __import__('modules.' + device_type, globals(), locals(), ['object'], -1)
    target_func = getattr(target_mod, func_name)
    return target_func(connection, *arg)


def get_bgp_memory_usage():
    func_name = 'get_bgp_memory_usage'

    def decorator(connection):
        def wrapper(connection):
            return _run_operation(connection, func_name)
        return wrapper
    return decorator


def get_bgp_neighbor():
    func_name = 'get_bgp_neighbor'

    def decorator(connection):
        def wrapper(connection, neighbor_address):
            return _run_operation(connection, func_name, neighbor_address)
        return wrapper
    return decorator


def get_bgp_neighbors():
    func_name = 'get_bgp_neighbors'

    def decorator(connection):
        def wrapper(connection):
            return _run_operation(connection, func_name)
        return wrapper
    return decorator


def get_bgp_summary():
    func_name = 'get_bgp_summary'

    def decorator(connection):
        def wrapper(connection):
            return _run_operation(connection, func_name)
        return wrapper
    return decorator


def get_interface_description():
    func_name = 'get_interface_description'

    def decorator(connection):
        def wrapper(connection, port_id):
            return _run_operation(connection, func_name, port_id)
        return wrapper
    return decorator


def get_interfaces_description():
    func_name = 'get_interfaces_description'

    def decorator(connection):
        def wrapper(connection):
            return _run_operation(connection, func_name)
        return wrapper
    return decorator


def get_interface_statistics():
    def decorator(connection):
        def wrapper(connection, port_id):
            return _run_operation(connection, func_name, port_id)
        return wrapper
    return decorator


def get_interfaces_statistics():
    func_name = 'get_interfaces_statistics'

    def decorator(connection):
        def wrapper(connection):
            return _run_operation(connection, func_name)
        return wrapper
    return decorator


def get_interfaces_mac_address():
    func_name = 'get_interfaces_mac_address'

    def decorator(connection):
        def wrapper(connection):
            return _run_operation(connection, func_name)
        return wrapper
    return decorator


def get_ipv6_addresses():
    func_name = 'get_ipv6_addresses'

    def decorator(connection):
        def wrapper(connection):
            return _run_operation(connection, func_name)
        return wrapper
    return decorator


def get_ipv6_ospf_interface():
    def decorator(connection):
        def wrapper(connection, port_id):
            return _run_operation(connection, func_name, port_id)
        return wrapper
    return decorator


def get_ipv6_ospf_interfaces():
    func_name = 'get_ipv6_ospf_interfaces'

    def decorator(connection):
        def wrapper(connection):
            return _run_operation(connection, func_name)
        return wrapper
    return decorator


def get_ipv6_ospf_neighbor_brief():
    def decorator(connection):
        def wrapper(connection, neighbor_rid):
            return _run_operation(connection, func_name, port_id)
        return wrapper
    return decorator


def get_ipv6_ospf_neighbor_detail():
    def decorator(connection):
        def wrapper(connection, neighbor_rid):
            return _run_operation(connection, func_name, neighbor_rid)
        return wrapper
    return decorator


def get_ipv6_ospf_neighbors_brief():
    func_name = 'get_ipv6_ospf_neighbors_brief'

    def decorator(connection):
        def wrapper(connection):
            return _run_operation(connection, func_name)
        return wrapper
    return decorator


def get_ipv6_ospf_neighbors_detail():
    func_name = 'get_ipv6_route_table'

    def decorator(connection):
        def wrapper(connection):
            return _run_operation(connection, func_name)
        return wrapper
    return decorator


def get_ipv6_route_table():
    func_name = 'get_ipv6_route_table'

    def decorator(connection):
        def wrapper(connection):
            return _run_operation(connection, func_name)
        return wrapper
    return decorator


def get_lldp_interface():
    def decorator(connection):
        def wrapper(connection, port_id):
            return _run_operation(connection, func_name, port_id)
        return wrapper
    return decorator


def get_lldp_neighbors():
    func_name = 'get_lldp_neighbors'

    def decorator(connection):
        def wrapper(connection):
            return _run_operation(connection, func_name)
        return wrapper
    return decorator


def get_ndp_table_reachable_entries():
    func_name = 'get_ndp_table_reachable_entries'

    def decorator(connection):
        def wrapper(connection):
            return _run_operation(connection, func_name)
        return wrapper
    return decorator


def get_ndp_table_stale_entries():
    func_name = 'get_ndp_table_stale_entries'

    def decorator(connection):
        def wrapper(connection):
            return _run_operation(connection, func_name)
        return wrapper
    return decorator


def get_ndp_table():
    func_name = 'get_ndp_table'

    def decorator(connection):
        def wrapper(connection):
            return _run_operation(connection, func_name)
        return wrapper
    return decorator


def get_system_info():
    func_name = 'get_system_info'

    def decorator(connection):
        def wrapper(connection):
            return _run_operation(connection, func_name)
        return wrapper
    return decorator


def get_system_uptime():
    func_name = 'get_system_uptime'

    def decorator(connection):
        def wrapper(connection):
            return _run_operation(connection, func_name)
        return wrapper
    return decorator
