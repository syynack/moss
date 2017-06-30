#!/usr/bin/env python

def get_bgp_memory_usage(connection):
    command = 'vtysh -c "show bgp memory"'
    output = connection.send_command(command)

    if output is None or 'failed' in output:
        return {
            'result': 'fail',
            'stdout': output
        }

    stdout = {"tables": []}

    for line in output.splitlines():
        line = line.split(',')

        if len(line) > 1:
            table_details = line[0].split()
            memory_usage = line[1].split()

            if memory_usage[3] == 'KiB':
                memory_usage[2] = int(memory_usage[2]) * 1024

            stdout["tables"].append({
                "table_id": '_'.join(table_details[1:]).lower().replace('-', '_'),
                "total": table_details[0],
                "mem_usage": ' '.join(memory_usage[1:3])
            })

    return {
        'result': 'success',
        'stdout': stdout
    }
