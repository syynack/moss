#!/usr/bin/env python

def get_ipv6_addresses(connection):
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
