#!/usr/bin/env python

def get_ndp_table(connection):
    '''
    Summary:
    Runs ip -6 neighbor show on a Linux box to retrieve the IPv6 Neighbor
    Discovery Protocol table.

    Example expected output of ip -6 neighbor show:

    fe80::70ad:19ff:fed3:4213/64 dev eth0 lladdr 00:18:4d:af:a0:64 REACHABLE

    Arguments:
    connection:         object, MossDeviceOrchestrator object

    Returns:
    list

    Example:
    "stdout": [
        {
            "inet6_addr": "fe80::70ad:19ff:fed3:4213/64",
            "port_id": "eth0",
            "ll_addr": "00:18:4d:af:a0:64",
            "state": "REACHABLE"
        }
    ]
    '''

    command = 'ip -6 neighbor show'
    output = connection.send_command(command)

    if output is None or 'not found' in output:
        return {
            'result': 'fail',
            'stdout': output
        }

    stdout = []
    regex = '(?P<inet6_addr>[^\s]+)\sdev\s(?P<port_id>[^\s]+)\slladdr\s(?P<ll_addr>[^\s]+)\srouter\s(?P<state>[^\n]+)'

    for line in output.splitlines():
        data = re.search(regex, line)
        if data is not None:
            data = data.groupdict()
            stdout.append(data)

    return {
        'result': 'success',
        'stdout': stdout
    }
