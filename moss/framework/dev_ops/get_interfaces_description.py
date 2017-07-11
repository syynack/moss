#!/usr/bin/env python

def linux_get_interfaces_description(connection):
    command = 'vtysh -c "show interface description" | tail -n +2'
    output = connection.send_command(command)

    if output is None or 'command not found' in output:
        return {
            'result': 'fail',
            'stdout': output
        }

    stdout = {}

    for line in output.splitlines():
        line = line.split()

        if len(line) > 0:
            stdout[line[0]] = {
                "admin_status": line[1],
                "line_status": line[2],
                "description": "" if len(line) < 4 else ' '.join(line[3:])
            }

    return {
        'result': 'success',
        'stdout': stdout
    }
