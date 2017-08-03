#!/usr/bin/env python

import re
from moss.framework.decorators import register

@register(platform = 'linux')
def linux_get_interfaces_statistics(connection):
    '''
    Summary:
    Runs ifconfig -a on a Linux box to retrieve information for all interfaces
    including tunnels and internal interfaces.

    Example expected output of ifconfig -a for an interface is:

    sit0      Link encap:IPv6-in-IPv4
              NOARP  MTU:1480  Metric:1
              RX packets:0 errors:0 dropped:0 overruns:0 frame:0
              TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:1
              RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

    Arguments:
    connection:         object, MossDeviceOrchestrator object

    Returns:
    dict

    Depends:
    net-tools

    Example:
    "stdout": {
        "sit0": {
            "collisions": "0",
            "link_encapsulation": "IPv6-in-IPv4",
            "mtu": "1480",
            "rx_bytes": "0",
            "rx_drp": "0",
            "rx_err": "0",
            "rx_frm": "0",
            "rx_ok": "0",
            "rx_ovr": "0",
            "rx_total": "0.0 B",
            "tx_bytes": "0",
            "tx_car": "0",
            "tx_drp": "0",
            "tx_err": "0",
            "tx_ok": "0",
            "tx_ovr": "0",
            "tx_queue_length": "1",
            "tx_total": "0.0 B"
        }
    }
    '''

    command = 'ifconfig -a'
    output = connection.send_command(command)

    if output is None or 'command not found' in output:
        return {
            'result': 'fail',
            'stdout': output
        }

    stdout = {}
    regexes = ['Link encap:(?P<link_encapsulation>[^\s]+)',
        'MTU:(?P<mtu>[^\s]+)',
        'RX\spackets:(?P<rx_ok>[^\s]+)\serrors:(?P<rx_err>[^\s]+)\sdropped:(?P<rx_drp>[^\s]+)\soverruns:(?P<rx_ovr>[^\s]+)\sframe:(?P<rx_frm>[^\s]+)',
        'TX\spackets:(?P<tx_ok>[^\s]+)\serrors:(?P<tx_err>[^\s]+)\sdropped:(?P<tx_drp>[^\s]+)\soverruns:(?P<tx_ovr>[^\s]+)\scarrier:(?P<tx_car>[^\s]+)',
        'collisions:(?P<collisions>[^\s]+)\stxqueuelen:(?P<tx_queue_length>[^\s]+)',
        'RX\sbytes:(?P<rx_bytes>[^\s]+)\s\(((?P<rx_total>[^)]+))\)',
        'TX\sbytes:(?P<tx_bytes>[^\s]+)\s\(((?P<tx_total>[^)]+))\)'
    ]

    for line in output.splitlines():
        if 'Link encap' in line:
            split_line = line.split()
            port_id = split_line[0]
            stdout[port_id] = {}

        for regex in regexes:
            match = re.search(regex, line)

            if match:
                stdout[port_id].update(match.groupdict())

    return {
        'result': 'success',
        'stdout': stdout
    }
