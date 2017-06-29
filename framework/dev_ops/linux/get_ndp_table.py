#!/usr/bin/env python

def get_ndp_table(connection):
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
