#!/usr/bin/env python

import re
from moss.framework.decorators import register

@register(platform = 'linux')
def linux_get_system_uptime(connection):
    '''
    Summary:
    Runs uptime on a Linux box to retrieve information regarding the uptime,
    users and CPU information.

    Example expected output of uptime:

     05:02:47 up 2 days,  7:38,  1 user,  load average: 0.00, 0.00, 0.00

    Arguments:
    connection:         object, MossDeviceOrchestrator object

    Returns:
    dict

    Example:
    "stdout": {
        "avg_15_min_load": "0.00",
        "avg_1_min_load": "0.00",
        "avg_5_min_load": "0.00",
        "current_time": "05:03:28",
        "uptime": "2 days",
        "users": "2"
    }
    '''

    command = 'uptime'
    output = connection.send_command(command)

    if output is None or 'not found' in output:
        return {
            'result': 'fail',
            'stdout': output
        }

    stdout = {}
    regexes = [
        '\s(?P<current_time>[0-9]{2}:[0-9]{2}:[0-9]{2})\sup',
        '\sup(?P<uptime>[^,]+)',
        ',(?P<users>.*)user.*load\saverage:',
        'load\saverage:(?P<avg_1_min_load>[^,]+),(?P<avg_5_min_load>[^,]+),(?P<avg_15_min_load>[^\n]+)'
    ]

    for line in output.splitlines():
        for regex in regexes:
            data = re.search(regex, line, re.MULTILINE)

            if data is not None:
                stdout.update(data.groupdict())

    for key, element in stdout.iteritems():
        stdout[key] = element.strip()

        if key == 'users':
            stdout['users'] = int(element)

    return {
        'result': 'success',
        'stdout': stdout
    }
