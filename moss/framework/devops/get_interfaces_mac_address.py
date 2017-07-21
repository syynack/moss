#!/usr/bin/env python

import re
from moss.framework.decorators import register

@register(platform = 'linux')
def linux_get_interfaces_mac_address(connection):
    '''
    Summary:
    Runs ifconfig on a Linux box to retrieve interface information, this
    should return the MAC address under the HWaddr tag.

    Example expected output of ifconfig for an interface is:

    eth0      Link encap:Ethernet  HWaddr 02:42:ac:11:00:02
              inet addr:172.17.0.2  Bcast:0.0.0.0  Mask:255.255.0.0
              inet6 addr: fe80::42:acff:fe11:2/64 Scope:Link
              UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
              RX packets:12821 errors:0 dropped:0 overruns:0 frame:0
              TX packets:10079 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:0
              RX bytes:1237182 (1.1 MiB)  TX bytes:1817168 (1.7 MiB)

    Arguments:
    connection:         object, MossDeviceOrchestrator object

    Returns:
    list

    Depends:
    net-tools

    Example:
    "stdout": [
        {
            "ll_addr": "02:42:ac:11:00:02",
            "port_id": "eth0"
        }
    ]
    '''

    command = 'ifconfig'
    output = connection.send_command(command)

    if output is None or 'not found' in output:
        return {
            'result': 'fail',
            'stdout': output
        }

    stdout = []
    regex = '(?P<port_id>([^\s]+)).*?\sHWaddr\s(?P<ll_addr>([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2}))'

    for line in output.splitlines():
        data = re.search(regex, line)
        if data is not None:
            stdout.append(data.groupdict())

    return {
        'result': 'success',
        'stdout': stdout
    }
