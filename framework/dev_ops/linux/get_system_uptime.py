#!/usr/bin/env python

import re

def get_system_uptime(connection):
    command = 'uptime'
    output = connection.send_command(command)

    if output is None or 'not found' in output:
        return {
            'result': 'fail',
            'stdout': output
        }

    stdout = {}
    regex = '\s(?P<current_time>[0-9]{2}:[0-9]{2}:[0-9]{2})\sup\s(?P<uptime>[^\s]+\s[^,]+).*' \
            '(?P<users>[0-9])\suser.*load\saverage:\s(?P<avg_1_min_load>[0-100].[0-9]{2}),' \
            '\s(?P<avg_5_min_load>[0-100].[0-9]{2}),\s(?P<avg_15_min_load>[0-100].[0-9]{2})'

    for line in output.splitlines():
        data = re.search(regex, line, re.MULTILINE)

        if data is not None:
            stdout.update(data.groupdict())

    return {
        'result': 'success',
        'stdout': stdout
    }
