#!/usr/bin/env python

from moss.register import register

@register(platform = 'linux')
def linux_get_ipv6_addresses(connection):
    '''
    Summary:
    Runs ifconfig on a Linux box grepping for link encapsulation and
    inet6 addresses.

    Example expected output of ifconfig | grep -E "(Link encap|inet6 addr)"
    for an interface is:

    eth0      Link encap:Ethernet  HWaddr 02:42:ac:11:00:02
              inet6 addr: fe80::42:acff:fe11:2/64 Scope:Link
    lo        Link encap:Local Loopback
              inet6 addr: ::1/128 Scope:Host

    Arguments:
    connection:         object, MossDeviceOrchestrator object

    Returns:
    dict

    Depends:
    net-tools

    Example:
    "stdout": {
        "eth0": [
            "fe80::42:acff:fe11:2/64"
        ],
        "lo": [
            "::1/128"
        ]
    }
    '''

    command = 'ifconfig | grep -E "(Link encap|inet6 addr)"'
    output = connection.send_command(command)

    if output is None or 'command not found' in output:
        return {
            'result': 'fail',
            'stdout': output
        }

    stdout = {}
    previous_port = ''

    for line in output.splitlines():
        if 'Link encap' in line:
            port_id = line.split()[0]
            previous_port = port_id

            if port_id not in stdout:
                stdout[port_id] = []

        elif 'inet6' in line:
            addr = line.split()[2]
            stdout[previous_port].append(addr)

    return {
        'result': 'success',
        'stdout': stdout
    }
