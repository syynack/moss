#!/usr/bin/env python

from dev_ops.linux import get_interfaces_statistics, get_interfaces_mac_address, \
                          get_ipv6_addresses, get_lldp_neighbors, \
                          get_ndp_table, get_system_info, get_system_uptime \

def linux_get_interface_statistics(connection):
    '''
    Summary:
    Returns detailed statistics JSON formatted data for a specific Linux
    interface.

    Arguments:
    connection:         object, MossDeviceOrchestrator

    Returns:
    dict
    '''

    task_info = {
        'namespace': 'interface',
        'task': 'get_interface_statistics',
        'platform': 'linux',
        'subtool': 'native'
    }

    output_dict = get_interfaces_statistics(connection)

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


def linux_get_interfaces_mac_address(connection):
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

    output_dict = get_interfaces_mac_address(connection)
    output_dict.update(task_info)
    return output_dict


def linux_get_interfaces_statistics(connection):
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

    output_dict = get_interfaces_statistics(connection)
    output_dict.update(task_info)
    return output_dict


def linux_get_ipv6_addresses(connection):
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

    output_dict = get_ipv6_addresses(connection)
    output_dict.update(task_info)
    return output_dict


<<<<<<< HEAD
def linux_get_lldp_interface(connection, port_id):
=======
def linux_get_lldp_interface(connection):
>>>>>>> 99871641558178efcc7ca47908586379a9900f6a
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

    output_dict = get_lldp_neighbors(connection)

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


def linux_get_lldp_neighbors(connection):
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

    output_dict = get_lldp_neighbors(connection)
    output_dict.update(task_info)
    return output_dict


def linux_get_ndp_table_reachable_entries(connection):
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

    output_dict = get_ndp_table(connection)

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


def linux_get_ndp_table_stale_entries(connection):
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

    output_dict = get_ndp_table(connection)

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


def linux_get_ndp_table(connection):
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

    output_dict = get_ndp_table(connection)
    output_dict.update(task_info)
    return output_dict


def linux_get_system_info(connection):
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

    output_dict = get_system_info(connection)
    output_dict.update(task_info)
    return output_dict


def linux_get_system_uptime(connection):
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

    output_dict = get_system_uptime(connection)
    output_dict.update(task_info)
    return output_dict
