#!/usr/bin/env python

import click

from moss.register import register
from moss.modules.dev_ops import linux_get_bgp_memory_usage, linux_get_bgp_neighbors, linux_get_bgp_summary, \
                                 linux_get_interfaces_description, linux_get_interfaces_mac_address, \
                                 linux_get_interfaces_statistics, linux_get_ipv6_addresses, \
                                 linux_get_ipv6_ospf_interfaces, linux_get_ipv6_ospf_neighbors_brief, \
                                 linux_get_ipv6_ospf_neighbors_detail, linux_get_ipv6_route_table, \
                                 linux_get_lldp_neighbors, linux_get_ndp_table, linux_get_system_info, \
                                 linux_get_system_uptime


@register(platform = 'linux')
def get_interface_statistics(connection, port_id):
    '''
    Summary:
    Returns detailed statistics JSON formatted data for a specific Linux
    interface.

    Arguments:
    connection:         object, MossDeviceOrchestrator
    port_id:            string, interface port ID

    Returns:
    dict
    '''

    task_info = {
        'namespace': 'interface',
        'task': 'get_interface_statistics',
        'platform': 'linux',
        'subtool': 'native'
    }

    output_dict = linux_get_interfaces_statistics(connection)

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


@register(platform = 'linux')
def get_interfaces_mac_address(connection):
    '''
    Summary:
    Returns the MAC address of recognised Linux Kernel interfaces.

    Arguments:
    connection:         object, MossDeviceOrchestrator

    Returns:
    dict
    '''

    task_info = {
        'namespace': 'mac',
        'task': 'get_interfaces_mac_address',
        'platform': 'linux',
        'subtool': 'native'
    }

    output_dict = linux_get_interfaces_mac_address(connection)
    output_dict.update(task_info)
    return output_dict


@register(platform = 'linux')
def get_interfaces_statistics(connection):
    '''
    Summary:
    Returns detailed statistics JSON formatted data for Linux interfaces

    Arguments:
    connection:         object, MossDeviceOrchestrator

    Returns:
    dict
    '''

    task_info = {
        'namespace': 'interface',
        'task': 'get_interfaces_statistics',
        'platform': 'linux',
        'subtool': 'native'
    }

    output_dict = linux_get_interfaces_statistics(connection)
    output_dict.update(task_info)
    return output_dict


@register(platform = 'linux')
def get_ipv6_addresses(connection):
    '''
    Summary:
    Return a JSON formatted output of ifconfig containing interface
    IPv6 link local and global addresses.

    Arguments:
    connection:         object, MossDeviceOrchestrator

    Returns:
    dict
    '''

    task_info = {
        'namespace': 'ipv6',
        'task': 'get_ipv6_addresses',
        'platform': 'linux',
        'subtool': 'native'
    }

    output_dict = linux_get_ipv6_addresses(connection)
    output_dict.update(task_info)
    return output_dict


@register(platform = 'linux')
def get_lldp_interface(connection, port_id):
    '''
    Summary:
    Return JSON formatted output of the Linux LLDP implementation
    lldpd, for a specific interface

    Arguments:
    connection:         object, MossDeviceOrchestrator
    port_id:            string, interface port ID

    Returns:
    dict
    '''

    task_info = {
        'namespace': 'lldp',
        'task': 'get_lldp_interface',
        'platform': 'linux',
        'subtool': 'lldpd'
    }

    output_dict = linux_get_lldp_neighbors(connection)

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


@register(platform = 'linux')
def get_lldp_neighbors(connection):
    '''
    Summary:
    Returns JSON formatted output of the lldpd daemon on Linux.

    Arguments:
    connection:         object, MossDeviceOrchestrator

    Returns:
    dict
    '''

    task_info = {
        'namespace': 'lldp',
        'task': 'get_lldp_neighbors',
        'platform': 'linux',
        'subtool': 'lldpd'
    }

    output_dict = linux_get_lldp_neighbors(connection)
    output_dict.update(task_info)
    return output_dict


@register(platform = 'linux')
def get_ndp_table_reachable_entries(connection):
    '''
    Summary:
    Returns the IPv6 Neighbor Discovery Protocol table in a JSON format
    and parses the output for reachable entries.

    Arguments:
    connection:         object, MossDeviceOrchestrator

    Returns:
    dict
    '''

    task_info = {
        'namespace': 'ndp',
        'task': 'get_ndp_table_reachable_entries',
        'platform': 'linux',
        'subtool': 'native'
    }

    output_dict = linux_get_ndp_table(connection)

    if output_dict['result'] == 'fail':
        output_dict.update(task_info)
        return output_dict

    stale_entries_dict = {}

    for entry in output_dict['stdout']:
        if entry['state'] == 'REACHABLE':
            stale_entries_dict.update(entry)

    output_dict['stdout'] = stale_entries_dict
    output_dict.update(task_info)
    return output_dict


@register(platform = 'linux')
def get_ndp_table_stale_entries(connection):
    '''
    Summary:
    Returns the IPv6 Neighbor Discovery Protocol table in a JSON format
    and parses the output for stale entries.

    Arguments:
    connection:         object, MossDeviceOrchestrator

    Returns:
    dict
    '''

    task_info = {
        'namespace': 'ndp',
        'task': 'get_ndp_table_stale_entries',
        'platform': 'linux',
        'subtool': 'native'
    }

    output_dict = linux_get_ndp_table(connection)

    if output_dict['result'] == 'fail':
        output_dict.update(task_info)
        return output_dict

    stale_entries_dict = {}

    for entry in output_dict['stdout']:
        if entry['state'] == 'STALE':
            stale_entries_dict.update(entry)

    output_dict['stdout'] = stale_entries_dict
    output_dict.update(task_info)
    return output_dict


@register(platform = 'linux')
def get_ndp_table(connection):
    '''
    Summary:
    Returns the IPv6 Neighbor Discovery Protocol table in a JSON format.

    Arguments:
    connection:         object, MossDeviceOrchestrator

    Returns:
    dict
    '''

    task_info = {
        'namespace': 'ndp',
        'task': 'get_ndp_table',
        'platform': 'linux',
        'subtool': 'native'
    }

    output_dict = linux_get_ndp_table(connection)
    output_dict.update(task_info)
    return output_dict


@register(platform = 'linux')
@click.option('-c', '--connection', required = True)
def get_system_info(connection):
    '''
    Summary:
    Runs 'uname' with additional on a linux box to return the system
    information: kernel name, hostname, kernel release, architecture,
    processor, hardware_platform, operating_system

    Arguments:
    connection:         object, MossDeviceOrchestrator

    Returns:
    dict
    '''

    task_info = {
        'namespace': 'system',
        'task': 'get_system_info',
        'platform': 'linux',
        'subtool': 'native'
    }

    output_dict = linux_get_system_info(connection)
    output_dict.update(task_info)
    return output_dict


@register(platform = 'linux')
def get_system_uptime(connection):
    '''
    Summary:
    Runs 'uptime' on a linux box to return the uptime status as well
    as CPU load, users, and current time

    Arguments:
    connection:         object, MossDeviceOrchestrator

    Returns:
    dict
    '''

    task_info = {
        'namespace': 'system',
        'task': 'get_system_uptime',
        'platform': 'linux',
        'subtool': 'native'
    }

    output_dict = linux_get_system_uptime(connection)
    output_dict.update(task_info)
    return output_dict


@register(platform = 'linux')
def get_bgp_memory_usage(connection):
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

    output_dict = linux_get_bgp_memory_usage(connection)
    output_dict.update(task_info)
    return output_dict


@register(platform = 'linux')
def get_bgp_neighbor(connection, neighbor_address):
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

    output_dict = linux_get_bgp_neighbors(connection)

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


@register(platform = 'linux')
def get_bgp_neighbors(connection):
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

    output_dict = linux_get_bgp_neighbors(connection)
    output_dict.update(task_info)
    return output_dict


@register(platform = 'linux')
def get_bgp_summary(connection):
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

    output_dict = linux_get_bgp_summary(connection)
    output_dict.update(task_info)
    return output_dict


@register(platform = 'linux')
def get_interface_description(connection, port_id):
    '''
    Summary:
    Returns JSON formatted data for a Quagga interface.

    Arguments:
    connection:         object, MossDeviceOrchestrator
    port_id:            string, interface port ID

    Returns:
    dict
    '''

    task_info = {
        'namespace': 'interface',
        'task': 'get_interface_description',
        'platform': 'linux',
        'subtool': 'quagga'
    }

    output_dict = linux_get_interfaces_description(connection)

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


@register(platform = 'linux')
def get_interfaces_description(connection):
    '''
    Summary:
    Returns JSON formatted data for Quagga interfaces.

    Arguments:
    connection:         object, MossDeviceOrchestrator

    Returns:
    dict
    '''

    task_info = {
        'namespace': 'interface',
        'task': 'get_interfaces_description',
        'platform': 'linux',
        'subtool': 'quagga'
    }

    output_dict = linux_get_interfaces_description(connection)
    output_dict.update(task_info)
    return output_dict


@register(platform = 'linux')
def get_ipv6_ospf_interface(connection, port_id):
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

    task_info = {
        'namespace': 'ospf',
        'task': 'get_ipv6_ospf_interface',
        'platform': 'linux',
        'subtool': 'quagga'
    }

    output_dict = linux_get_ipv6_ospf_interfaces(connection)

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


@register(platform = 'linux')
def get_ipv6_ospf_interfaces(connection):
    '''
    Summary:
    Returns JSON data for all IPv6 OSPFv3 interfaces.

    Arguments:
    connection:         object, MossDeviceOrchestrator

    Returns:
    dict
    '''

    task_info = {
        'namespace': 'ospf',
        'task': 'get_ipv6_ospf_interfaces',
        'platform': 'linux',
        'subtool': 'quagga'
    }

    output_dict = linux_get_ipv6_ospf_interfaces(connection)
    output_dict.update(task_info)
    return output_dict


@register(platform = 'linux')
def get_ipv6_ospf_neighbor_brief(connection, neighbor_rid):
    '''
    Summary:
    Return JSON data for a specific OSPFv3 neighbor in a brief format.

    Arguments:
    connection:         object, MossDeviceOrchestrator
    neighbor_rid:       string, OSPFv3 neighbor Router ID

    Returns:
    dict
    '''

    task_info = {
        'namespace': 'ospf',
        'task': 'get_ipv6_ospf_neighbor_brief',
        'platform': 'linux',
        'subtool': 'quagga'
    }

    output_dict = linux_get_ipv6_ospf_neighbors_brief(connection)

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


@register(platform = 'linux')
def get_ipv6_ospf_neighbor_detail(connection, neighbor_rid):
    '''
    Summary:
    Return JSON data for a specific OSPFv3 neighbor in a detailed format.

    Arguments:
    connection:         object, MossDeviceOrchestrator
    neighbor_rid:       string, OSPFv3 neighbor Router ID

    Returns:
    dict
    '''

    task_info = {
        'namespace': 'ospf',
        'task': 'get_ipv6_ospf_neighbor_detail',
        'platform': 'linux',
        'subtool': 'quagga'
    }

    output_dict = linux_get_ipv6_ospf_neighbors_detail(connection)

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


@register(platform = 'linux')
def get_ipv6_ospf_neighbors_brief(connection):
    '''
    Summary:
    Returns JSON data for all IPv6 OSPFv3 neighbors in a brief format.

    Arguments:
    connection:         object, MossDeviceOrchestrator

    Returns:
    dict
    '''

    task_info = {
        'namespace': 'ospf',
        'task': 'get_ipv6_ospf_neighbors_brief',
        'platform': 'linux',
        'subtool': 'quagga'
    }

    output_dict = linux_get_ipv6_ospf_neighbors_brief(connection)
    output_dict.update(task_info)
    return output_dict


@register(platform = 'linux')
def get_ipv6_ospf_neighbors_detail(connection):
    '''
    Summary:
    Returns JSON data for all IPv6 OSPFv3 neighbors in a detailed format.

    Arguments:
    connection:         object, MossDeviceOrchestrator

    Returns:
    dict
    '''

    task_info = {
        'namespace': 'ospf',
        'task': 'get_ipv6_ospf_neighbors_detail',
        'platform': 'linux',
        'subtool': 'quagga'
    }

    output_dict = linux_get_ipv6_ospf_neighbors_detail(connection)
    output_dict.update(task_info)
    return output_dict


@register(platform = 'linux')
def get_ipv6_route_table(connection):
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
        'task': 'get_ipv6_route_table',
        'platform': 'linux',
        'subtool': 'quagga'
    }

    output_dict = linux_get_ipv6_route_table(connection)
    output_dict.update(task_info)
    return output_dict
